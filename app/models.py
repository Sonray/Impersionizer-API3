
from . import db

class User(db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(55), unique = True)
    email = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(80))

    def __repr__(self):
        return f'User {self.username, self.email, self.password}'