from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = '770fcd875ec5d962f02de6b54854df98'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)

from covid19.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


from covid19 import routes
from covid19.models import User, Posts
