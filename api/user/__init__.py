from flask_restx import Resource, Api, Namespace

User = Namespace(name='Users', description="User Login & SigIn API")


@User.route('')
class Users(Resource):
    def post(self):
        return {}, 201
