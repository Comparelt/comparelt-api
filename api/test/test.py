import os
import tempfile
import unittest
from api import comparelt


class TestCase(unittest.TestCase):

    def setUp(self):
        self.db, comparelt.app.config['DATABASE'] = tempfile.mkstemp()
        comparelt.app.config['TESTING'] = True
        self.app = comparelt.app.test_client()
        comparelt.init_db()

    def signup(self, username, email, password):
        return self.app.post('/signup', data=dict(
            username=username,
            email=email,
            password=password
        ), follow_redirects=True)

    def login(self, email, password):
        return self.app.post('/login', data=dict(
            email=email,
            password=password
        ), follow_redirects=True)

    def test_signup(self):
        user_test = self.signup('dku', 'dku@test.com', 'dku@20')
        print(user_test)

    def test_login(self):
        user_test = self.login('dku@test.com', 'dku@20')
        print(user_test)

    def tearDown(self):
        os.close(self.db)
        os.unlink(comparelt.app.config['DATABASE'])


if __name__ == '__main__':
    unittest.main()