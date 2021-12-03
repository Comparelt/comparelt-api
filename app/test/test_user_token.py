import unittest

import bcrypt

from app.main import db
from app.main.model.user import User
from app.test.setup import SetupTestCase


class TestUserModel(SetupTestCase):

    def test_d_encode_auth_token(self):
        user = User(
            username='test',
            email='test@test.com',
            hashed_password=bcrypt.hashpw(bytes('test', 'utf-8'), bcrypt.gensalt())
        )
        db.session.add(user)
        db.session.commit()
        auth_token = User.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))

    def test_e_decode_auth_token(self):
        user = User(
            username='test',
            email='test@test.com',
            hashed_password=bcrypt.hashpw(bytes('test', 'utf-8'), bcrypt.gensalt())
        )
        db.session.add(user)
        db.session.commit()
        auth_token = User.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue(User.decode_auth_token(auth_token.decode("utf-8")) == 1)


if __name__ == '__main__':
    unittest.main()
