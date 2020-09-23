from . import db

class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(55), unique = True)
    email = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(80))