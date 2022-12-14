from app import app
from flask import redirect, render_template, request, session
from db import db, fetch_lessons, feth_user_bookings
from db import save_user, check_password

@app.route("/")
def index():
    return render_template("index.html", )

@app.route("/home", methods=["GET"])
def home():
    usrname = session["username"]
    lessons = feth_user_bookings(db, usrname)
    return render_template("home.html", lessons=lessons)


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    success = check_password(db, username, password)
    if success == True:
        session["username"] = username
    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/registration_form")
def registration_form():
    return render_template("sign_up.html")

@app.route("/sign_up", methods=["POST"])
def register_user():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return redirect("/registration_form")
    success = save_user(db, username, password1)
    if success == False:
        return redirect("/registration_form")
    return redirect("/")

@app.route("/new_lesson")
def new_lesson():
    return render_template("new_lesson.html")

@app.route("/add_lesson")
def add_lesson():
    return redirect("/")