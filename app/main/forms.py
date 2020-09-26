from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, BooleanField, SelectField
from wtforms.validators import InputRequired, Email, Length


class SignUpForm(FlaskForm):
    username = StringField('Enter User-Name', validators=[InputRequired(), Length(max=20)])
    email = StringField('Enter Your Email',  validators=[InputRequired(), Email(message='Invalid Email')])
    password = PasswordField('Enter password', validators=[InputRequired(), Length(min=8, max=50)])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Enter User-Name', validators=[InputRequired(), Length(max=20)])
    password = PasswordField('Enter password', validators=[InputRequired(), Length(min=8, max=50)])
    remember = BooleanField()
    submit = SubmitField('Sign Up')

class PitchForm(FlaskForm):
    message = TextAreaField('Enter your pitch', validators=[InputRequired(), Length(max=255)])
    category = SelectField('Select pitch category', choices=[('technology', 'technology'), ('business', 'business'), ('politics', 'politics'), 
    ('art', 'art'), ('sports', 'sports'), ('music', 'music'), ('travel', 'travel')], validators=[InputRequired()] )
    submit = SubmitField('Post')