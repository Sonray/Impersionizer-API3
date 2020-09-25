
from . import db

class User(db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(55), unique = True)
    email = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(90))
    child = db.relationship('Child', backref= 'parent')

    def __repr__(self):
        return f'User {self.username, self.email, self.password}'

class Pitch(db.Model):

    __tablename__ = 'Pitches'
    id = db.Column(db.Integer, primary_key=True)
    pitch = db.Column(db.String(255), unique = True)
    User_id = db.Column(db.Integer, db.ForeignKey=('User.id') )

    def __repr__(self):
        return f'Pitch {self.pitch}'