from app import app
from flask_sqlalchemy import SQLAlchemy
from models import User
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

def save_user(database, username: str, password: str):
    result = database.session.execute("SELECT id, password FROM users WHERE username=:username", {"username":username})
    user = result.fetchone()
    if user:
        return False
    else:
        hash_value = generate_password_hash(password)
        sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
        return True

def check_password(database, username: str, password: str):
    result = database.session.execute("SELECT id, password FROM users WHERE username=:username", {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            return True
        else:
            return False