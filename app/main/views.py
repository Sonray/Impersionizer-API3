from flask import Flask, render_template, request, redirect, url_for
from . import main
from .. import db
from .forms import SignUpForm, LoginForm
from app.models import User
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
        #return '<h1>' + form.username.data + form.email.data + form.password.data + '<h1>'
        new_user = User(username = form.username.data, email = form.email.data, password = form.password.data)
        db.session.add(new_user)
        db.session.commit()

        return '<h1>Welcome </h1>'

    return render_template('signup.html', form=form)


@main.route('/login', methods = ['POST', 'GET'])
def lod_in():
    
    form = LoginForm()

    if form.validate_on_submit():
        #return '<h1>' + form.email.data + form.password.data + '<h1>'
        user = User.query.filter_by(username = form.username.data).first()

        if user:
            if user.password == form.password.data:
                return '<h1> login success </h1>'

        return '<h1> inavalid username </h1>'

    return render_template('login.html', form=form)
