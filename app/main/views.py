from flask import Flask, render_template, request, redirect, url_for
from . import main
from .. import db, login_manager
from .forms import SignUpForm, LoginForm, PitchForm
from app.models import User, Pitch
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, current_user, login_user, logout_user, current_user

login_manager.login_view = 'main.login'
@login_manager.user_loader
def load_user(User_id):
    return User.query.get(int(User_id))

#views
@main.route('/')
def index():
    hunt = 'hello world'
    return render_template('index.html', hunt=hunt)


@main.route('/sign', methods = ['POST', 'GET'])
def sign():
    form = SignUpForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        #return '<h1>' + form.username.data + form.email.data + form.password.data + '<h1>'
        new_user = User(username = form.username.data, email = form.email.data, password = hashed_password )
        db.session.add(new_user)
        db.session.commit()

        return '<h1>Welcome'+  hashed_password +' </h1>'

    return render_template('signup.html', form=form)


@main.route('/login', methods = ['POST', 'GET'])
def login():
    
    form = LoginForm()

    if form.validate_on_submit():
        
        user = User.query.filter_by(username = form.username.data).first()

        if user:
            if  check_password_hash( user.password, form.password.data):
                return '<h1> login success </h1>'

        return '<h1> inavalid username </h1>'

    return render_template('login.html', form=form)

@main.route('/dashboard', methods = ['POST', 'GET'])
@login_required
def dashboard():
    
    form = PitchForm()

    if form.validate_on_submit():

        new_pitch = Pitch(pitch = form.message.data)
        db.session.add(new_pitch)
        db.session.commit()

        return '<h1>Welcome </h1>'

    return render_template('dashboard.html', form=form)
