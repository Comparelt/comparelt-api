import os
import tempfile
import unittest
from api import comparelt


class AuthCase(unittest.TestCase):
    def setUp(self):
        self.db, comparelt.app.config['DATABASE'] = tempfile.mkstemp()
        comparelt.app.config['TESTING'] = True
        self.app = comparelt.app.test_client()
        comparelt.init_db()

    def signup(self, username, email, password):
        return self.app.post('/auth/signup', data={
            "email": email,
            "password": password,
            "username": username,
        })

    def test_a_signup(self):
        user_test = self.signup('dku', 'dku@test.com', 'dku@20')
        print(user_test)  # Need to add success case

    def login(self, email, password):
        return self.app.post('/auth/login', data={
            "email": email,
            "password": password,
        })

    def test_b_login(self):
        user_test = self.login('dku@test.com', 'dku@20')
        print(user_test) # Need to add success case

    def tearDown(self):
        os.close(self.db)
        os.unlink(comparelt.app.config['DATABASE'])


if __name__ == '__main__':
    unittest.main()