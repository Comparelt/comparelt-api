import bcrypt
import jwt
from flask import request
from flask_restx import Namespace, Resource, fields

Auth = Namespace(name="Auth", description="Auth API")

users = {}  # Need to add Get user data from database

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
        email = request.json['email']
        password = request.json['password']
        if email in users:
            return {
                       "message": "Duplicated user"
                   }, 409
        else:
            users[email] = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())  # save password
            return {
                       'Authorization': jwt.encode({'email': email}, "secret", algorithm="HS256").decode("UTF-8")  #
                   }, 200


@Auth.route('/login')
class AuthLogin(Resource):
    @Auth.expect(user_fields_auth)
    @Auth.doc(responses={200: 'Success'})
    @Auth.doc(responses={401: 'UnAuthorized'})
    @Auth.doc(responses={404: 'User Not Found'})
    def post(self):
        email = request.json['email']
        password = request.json['password']
        if email not in users:
            return {
                       "message": "User Not Found"
                   }, 404
        elif not bcrypt.checkpw(password.encode('utf-8'), users[email]):  # If password is correct
            return {
                       "message": "Auth Failed"
                   }, 401
        else:
            return {
                       'Authorization': jwt.encode({'email': email}, "secret", algorithm="HS256").decode("UTF-8")
                       # return as String
                   }, 200


@Auth.route('/get')
class AuthGet(Resource):
    @Auth.header(name='JWT',
                 description='Authorization which you must included in header', example="eyJ0eo02e5tg")
    @Auth.doc(responses={200: 'Success'})
    @Auth.doc(responses={401: 'Login Failed'})
    def get(self):
        header = request.headers.get('Authorization')  # Authorization into request header
        if header is None:
            return {"message": "Please Login"}, 401
        data = jwt.decode(header, "secret", algorithm="HS256")
        return data, 200
