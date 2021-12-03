import json
import unittest

from app.test.setup import SetupTestCase


def signup_user(self):
    return self.client.post(
        '/auth/signup',
        data=json.dumps(dict(
            email='dku@test.com',
            username='test_start',
            password='dku@20'
        )),
        content_type='application/json'
    )


def login_user(self):
    return self.client.post(
        '/auth/login',
        data=json.dumps(dict(
            email='dku@test.com',
            password='dku@20'
        )),
        content_type='application/json'
    )


class AuthTestCase(SetupTestCase):
    def test_a_signup(self):
        with self.client:
            response = signup_user(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['Authorization'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_b_signup_with_signed_user(self):
        signup_user(self)
        with self.client:
            response = signup_user(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 409)

    def test_c_user_login(self):
        with self.client:

            # user signup
            resp_signup = signup_user(self)
            data_signup = json.loads(resp_signup.data.decode())
            self.assertTrue(data_signup['status'] == 'success')
            self.assertTrue(data_signup['Authorization'])
            self.assertTrue(resp_signup.content_type == 'application/json')
            self.assertEqual(resp_signup.status_code, 201)

            # signed user login
            response = login_user(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['Authorization'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

    if __name__ == '__main__':
        unittest.main()