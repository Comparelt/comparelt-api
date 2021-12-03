from flask_restx import Resource

from app.main.service.user_service import UserService
from app.main.util.dto import UserDto

api = UserDto.api
_user = UserDto.user


@api.route('/<id>')
@api.param('id', 'User id')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user with id')
    @api.marshal_with(_user)
    def get(self, public_id):
        user = UserService.get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user
