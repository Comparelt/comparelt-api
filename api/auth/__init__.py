from flask_restx import Namespace, Resource

Auth = Namespace(name="Auth", description="Auth API")


@Auth.route('')
class Authentication(Resource):
    def get(self):
        return {}, 200

    def post(self):
        return {}, 201
