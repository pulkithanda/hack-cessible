from flask import Flask
from flask.templating import render_template
from covid19 import app
from covid19.forms import RegistrationForm


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


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title="Register", form=form)
