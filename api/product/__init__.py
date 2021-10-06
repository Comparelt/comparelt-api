from flask_restx import Namespace, Resource

Product = Namespace(name="Product", description="Product API")


@Product.route('')
class Products(Resource):
    def get(self):
        return {}, 200

    def post(self):
        return {}, 201