
from . import db, login_manager
from flask_login import UserMixin

class User(UserMixin, db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(55), unique = True)
    email = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(90))
    child = db.relationship('Pitch', backref= 'User', uselist=True )
    like = db.relationship('Likes', backref= 'likes', uselist=True )
    dislike = db.relationship('Dislikes', backref= 'dislikes', uselist=True )

    def __repr__(self):
        return f'User {self.username, self.email, self.password}'

class Pitch(UserMixin, db.Model):

    __tablename__ = 'Pitches'
    id = db.Column(db.Integer, primary_key=True)
    pitch = db.Column(db.String(255))
    category = db.Column(db.String(255))
    User_id = db.Column(db.Integer, db.ForeignKey('user.id') )
    liked = db.relationship('Likes', backref='liked')
    disliked = db.relationship('Dislike', backref='disliked')

    def __repr__(self):
        return f'Pitch {self.pitch, self.category }'

class Likes(UserMixin, db.Model):
    __tablename__ = 'Likes'
    id = db.Column(db.Integer, primary_key=True)
    User_id = db.Column(db.Integer, db.ForeignKey('user.id') )
    Pitch_id = db.Column(db.Integer, db.ForeignKey('Pitches.id') )

    def __repr__(self):
        return f'Pitch {self.User_id, self.Pitch_id }'

class Dislikes(UserMixin, db.Model):
    __tablename__ = 'Likes'
    id = db.Column(db.Integer, primary_key=True)
    User_id = db.Column(db.Integer, db.ForeignKey('user.id') )
    Pitch_id = db.Column(db.Integer, db.ForeignKey('Pitches.id') )

    def __repr__(self):
        return f'Pitch {self.User_id, self.Pitch_id }'
