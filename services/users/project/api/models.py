# services/users/project/api/models.py


from sqlalchemy.sql import func

from project import db


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(16), nullable=False)
    video = db.Column(db.String(128))
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, username, email, password, video):
        self.username = username
        self.email = email
        self.password = password
        self.video = video

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'video': self.video,
            'active': self.active
        }
