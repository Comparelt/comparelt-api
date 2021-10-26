from api import db
from api.common.ORMModel import ORMModel

#authorize a user for login & sign up part

class User(ORMModel):
    __tablename__ = 'user'

    # declare User Table Columns
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'username': self.username,
            'email': self.email,
            'password':  self.password,
        }
