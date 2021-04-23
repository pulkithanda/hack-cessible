from flask import Flask
from flask.templating import render_template
from covid19 import app


@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")
