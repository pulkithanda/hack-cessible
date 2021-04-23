from wtforms import PasswordField, SubmitField, StringField
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
        emailval = User.query.filter_by(email=email.data).first()
        if emailval:
            raise ValidationError(
                "There is already an account with this email address")
