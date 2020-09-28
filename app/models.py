
from . import db, login_manager
from flask_login import UserMixin

class User(UserMixin, db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(55), unique = True)
    email = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(90))
    child = db.relationship('Pitch', backref= 'the_User' )
    delike = db.relationship('Like', backref= 'likes' )
    dislike = db.relationship('Dislike', backref= 'dislikes' )

    def __repr__(self):
        return f'User {self.username, self.email, self.password}'

class Pitch(UserMixin, db.Model):

    __tablename__ = 'Pitches'
    id = db.Column(db.Integer, primary_key=True)
    pitch = db.Column(db.String(255))
    category = db.Column(db.String(255))
    User_id = db.Column(db.Integer, db.ForeignKey('user.id') )
    liked = db.relationship('Like', backref='liked')
    disliked = db.relationship('Dislike', backref='disliked')

    def __repr__(self):
        return f'Pitch {self.pitch, self.category }'

class Like(UserMixin, db.Model):
    __tablename__ = 'Likes'
    id = db.Column(db.Integer, primary_key=True)
    User_id = db.Column(db.Integer, db.ForeignKey('user.id') )
    Pitch_id = db.Column(db.Integer, db.ForeignKey('Pitches.id') )

    def __repr__(self):
        return f'Likes {self.User_id, self.Pitch_id }'

class Dislike(UserMixin, db.Model):
    __tablename__ = 'Dislikes'
    id = db.Column(db.Integer, primary_key=True)
    User_id = db.Column(db.Integer, db.ForeignKey('user.id') )
    Pitch_id = db.Column(db.Integer, db.ForeignKey('Pitches.id') )

    def __repr__(self):
        return f'Dislikes {self.User_id, self.Pitch_id }'
