from flask import render_template,request,redirect,url_for
from . import main
from .forms import Sign_up_form

#views
@main.route('/')
def index():
    return render_template('index.hmtl')

@main.route('/signup')
def signup():
    form = Sign_up_form()
    return render_template('signup.html', form = form)