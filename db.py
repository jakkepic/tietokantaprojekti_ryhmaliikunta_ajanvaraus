from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash
from entities import Lesson

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL").replace("://", "ql://", 1)
db = SQLAlchemy(app)


# functions for saving data to database
def save_user(database, username: str, password: str):
    result = database.session.execute("SELECT id, password FROM users WHERE username=:username", {"username":username})
    user = result.fetchone()
    if user:
        return False
    else:
        hash_value = generate_password_hash(password)
        sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
        database.session.execute(sql, {"username":username, "password":hash_value})
        database.session.commit()
        return True

def save_lesson(database, lesson: Lesson):
    sql = "INSERT INTO classes (classname) VALUES (:classname)"
    db.session.execute(sql, {"classname":lesson.name})
    db.session.commit()

# functions for fetching data from database
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

def fetch_lessons(database):
    result = database.session.execute("SELECT id, classname FROM classes")
    data = result.fetchall()
    entries = []
    for entry in data:
        lesson = Lesson(entry[1])
        entries.append(lesson)
    return entries

def fetch_lesson_name(database, classid):
    result = database.session.execute("SELECT classname FROM classes WHERE id=:classid", {"classid":classid})
    data = result.fetchone()
    return data[0]
    

def fetch_userid(database, username):
    result = database.session.execute("SELECT id FROM users WHERE username=:username", {"username":username})
    data = result.fetchone()
    return data[0]

def feth_user_bookings(database, username):
    userid = fetch_userid(database, username)
    result = database.session.execute("SELECT classid FROM bookings WHERE userid=:userid", {"userid":userid})
    data = result.fetchall()
    bookings = []
    for entry in data:
        lesson = Lesson(entry[0])
        lesson_name = fetch_lesson_name(database, lesson)
        bookings.append((lesson, lesson_name))
    return bookings