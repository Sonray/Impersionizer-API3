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

@main.route('/sign', methods = ['POST', 'GET'])
def sign():
    form = SignUpForm()

    if form.validate_on_submit():
        return '<h1>' + form.username.data + form.email.data + form.password.data + '<h1>'

    return render_template('signup.html', form=form)


@main.route('/login', methods = ['POST', 'GET'])
def lod_in():
    form = LoginForm()

    if form.validate_on_submit():
        return '<h1>' + form.email.data + form.password.data + '<h1>'

    return render_template('login.html', form=form)
