from flask import Flask
from flask.templating import render_template
from covid19 import app


@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/login")
def login():
    return render_template("login.html", title="Login")


@app.route("/register")
def register():
    return render_template('register.html', title="Register")
