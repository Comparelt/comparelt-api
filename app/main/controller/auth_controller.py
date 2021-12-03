from flask import request
from flask_restx import Resource

from ..service.auth_service import AuthService
from ..service.user_service import UserService
from ..util.dto import AuthDto, UserDto
from typing import Dict, Tuple

api = AuthDto.api
user_auth = AuthDto.user_auth
_user = UserDto.user


@api.route('/signup')
class UserSignUp(Resource):
    @api.doc('user signup')
    @api.expect(_user, validate=True)
    def post(self) -> Tuple[Dict[str, str], int]:
        data = request.json
        return UserService.save_new_user(data=data)


@api.route('/login')
class UserLogin(Resource):
    @api.doc('user login')
    @api.response(201, 'User created successfully')
    @api.expect(user_auth, validate=True)
    def post(self) -> Tuple[Dict[str, str], int]:
        post_data = request.json
        return AuthService.login_user(data=post_data)


@api.route('/logout')
class LogoutAPI(Resource):
    @api.doc('logout a user')
    def post(self) -> Tuple[Dict[str, str], int]:
        auth_header = request.headers.get('Authorization')
        return AuthService.logout_user(data=auth_header)