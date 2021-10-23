from flask_restx import Resource, Namespace

User = Namespace(name='Users', description="User API")


@User.route('')
class Users(Resource):
    def get(self):
        return {}, 200

    def post(self):
        return {}, 201