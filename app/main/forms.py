from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField

class Sign_up_form(FlaskForm):
    Username = StringField('Enter User-Name')
    Password = PasswordField('Enter password')
    Submit = ('Sign Up')