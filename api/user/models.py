from api import db


class User(db.Model):
    __tablename__ = 'user'

    # declare User Table Columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.name)

    def serialize(self):
        return {
            'username': self.username,
            'email': self.email,
            'password':  self.password,
        }