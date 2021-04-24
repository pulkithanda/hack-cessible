from flask import Flask, redirect, request
from flask.helpers import flash, url_for
from flask_login import login_user, current_user
from flask.templating import render_template
from covid19 import app, login_manager, db
from covid19.forms import RegistrationForm, LoginForm
from covid19.models import User
import bcrypt


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
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('Successfully logged in', 'success')
            return redirect(url_for('home'))
    return render_template("login.html", title="Login", form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == "POST":
        if form.validate_on_submit():
            print(form.email.data)
            if User.query.filter_by(email=form.email.data):
                flash("An acc   ount with this email address already exists")
                return redirect(url_for('login'))
            hashed_pw = bcrypt.generate_password_has(
                form.password.data).decode('UTF-8')
            user = User(email=form.email.data,
                        password=hashed_pw, phone=form.phone.data)
            db.session.add(user)
            db.session.commit()

    return render_template('register.html', title="Register", form=form)


'''
from flask_login import login_required, current_user

@app.route("/post", methods=['GET, POST'])
@login_required
def postCreate():
    return render_template('postCreate.html', title="Create Post", name=current_user)
'''
