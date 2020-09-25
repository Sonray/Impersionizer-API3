from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Email, Length


class SignUpForm(FlaskForm):
    username = StringField('Enter User-Name', validators=[InputRequired(), Length(max=20)])
    email = StringField('Enter Your Email',  validators=[InputRequired(), Email(message='Invalid Email')])
    password = PasswordField('Enter password', validators=[InputRequired(), Length(min=8, max=50)])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Enter User-Name', validators=[InputRequired(), Length(max=20)])
    password = PasswordField('Enter password', validators=[InputRequired(), Length(min=8, max=50)])
    submit = SubmitField('Sign Up')

class PitchForm(FlaskForm):
    message = TextAreaField('Enter your pitch', validators=[InputRequired(), Length(max=255)])
    submit = SubmitField('Post')