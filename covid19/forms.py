# from _typeshed import FileDescriptor
from flask.app import Flask
from wtforms import PasswordField, SubmitField, StringField
from wtforms.fields.core import BooleanField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError
from covid19.models import User, Posts
from flask_wtf import FlaskForm


class RegistrationForm(FlaskForm):
    email = StringField("email", validators=[DataRequired(), Length(2, 120)])
    password = PasswordField('password', validators=[
                             DataRequired(), Length(min=6)])
    confirm_password = PasswordField('confirm_password', validators=[
                                     DataRequired(), EqualTo('password')])
    phone = StringField("phone", validators=[DataRequired(), Length(10, 13)])
    submit = SubmitField("Sign Up")

    def validate_email(self, email):
        if User:
            emailval = User.query.filter_by(email=email.data).first()
            if emailval:
                raise ValidationError(
                    "There is already an account with this email. Please log in instead")
        else:
            pass


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Length(2, 120)])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=6, message="Invalid password. Passwords must be at least 6 characters long.")])
    remember = BooleanField('Remember Me')
    submit = SubmitField("Login")

    def validate_login(self, email, password):
        emailval = User.query.filter_by(email=email.data).first()
        if not emailval:
            raise ValidationError("No account with this email address exists")
        if password.data != emailval.password:
            raise ValidationError("Incorrect email address or password")
        return True


class CreatePostForm(FlaskForm):
    item = StringField("Medical Item", validators=[DataRequired()])
    city = StringField("City", validators=[DataRequired()])
    descrip = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField("Create Post")
