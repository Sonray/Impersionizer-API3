from flask import Flask, render_template, request, redirect, url_for
from . import main
from .forms import SignUpForm, LoginForm
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Email, Length




#views
@main.route('/')
def index():
    hunt = 'hello world'
    return render_template('index.html', hunt=hunt)

@main.route('/sign')
def sign():
    form = SignUpForm()
    return render_template('signup.html', form=form)


@main.route('/login')
def lod_in():
    form = LoginForm()
    return render_template('login.html', form=form)
