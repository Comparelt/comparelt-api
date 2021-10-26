from flask import request, jsonify
from flask_restx import Namespace, Resource, fields

from api.auth.service import AuthService

Auth = Namespace(name="Auth", description="Auth API")

user_fields = Auth.model('Email', {
    'email': fields.String(description='A User Email', required=True, example="dku@example.com")
})

user_fields_auth = Auth.inherit('User Auth', user_fields, {
    'password': fields.String(description='Password', required=True, example="password"),
    'username': fields.String(description='Username', required=True, example='dku')
})


@Auth.route('/signup')
class AuthRegister(Resource):
    @Auth.expect(user_fields_auth)
    @Auth.doc(responses={200: 'Success'})
    @Auth.doc(responses={409: 'Duplicated user'})
    def post(self):
        data = jsonify(request.form).json
        return AuthService.signup(data)


@Auth.route('/login')
class AuthLogin(Resource):
    @Auth.expect(user_fields_auth)
    @Auth.doc(responses={200: 'Success'})
    @Auth.doc(responses={401: 'UnAuthorized'})
    @Auth.doc(responses={404: 'User Not Found'})
    def post(self):
        data = jsonify(request.form).json
        email = data['email']
        password = data['password']
        return AuthService.login_with_email(email, password)
