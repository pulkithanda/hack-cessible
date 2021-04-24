from flask import Flask
import flask_login
from flask.templating import render_template
from covid19 import app, login_manager
from covid19.forms import RegistrationForm, LoginForm
from covid19.models import User


@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(user, remember=remember)
        '''return flask.redirect(flask.url_for('post'), title="Create Post")'''
    return render_template("login.html", title="Login", form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title="Register", form=form)


'''
from flask_login import login_required, current_user

@app.route("/post", methods=['GET, POST'])
@login_required
def postCreate():
    return render_template('postCreate.html', title="Create Post", name=current_user)
'''
