from typing import Union

import jwt

from app.main import db, flask_bcrypt
from app.main.config import key
from app.main.model.expire_token import ExpiredToken
from app.main.util.ORMModel import ORMModel


# authorize a user for login & sign up part

class User(ORMModel):
    __tablename__ = 'user'

    # declare User Table Columns
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    hashed_password = db.Column(db.String)

    def __init__(self, username, email, hashed_password, **kwargs):
        super().__init__(**kwargs)
        self.username = username
        self.email = email
        self.hashed_password = hashed_password

    def __repr__(self):
        return '<User %r>' % self.username

    @staticmethod
    def serialize(username, email, hashed_password):
        return {
            'username': username,
            'email': email,
            'password': hashed_password,
        }

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.hashed_password = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password: str) -> bool:
        return flask_bcrypt.check_password_hash(self.hashed_password, password)

    @staticmethod
    def encode_auth_token(user_id: int) -> Union[bytes, Exception]:
        try:
            payload = {
                'sub': user_id
            }
            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as e:
            print(e)
            return e

    @staticmethod
    def decode_auth_token(auth_token: str) -> Union[str, int]:
        try:
            payload = jwt.decode(auth_token, key)
            is_expired_token = ExpiredToken.check_expire(auth_token)
            if is_expired_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
