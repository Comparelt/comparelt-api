from flask_restx import Namespace, Resource, reqparse
from api.product.service import *
Product = Namespace(name="Product", description="Product API")


@Product.route('')
class Products(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('productTitle', type=str)
        args = parser.parse_args()

        _productTitle = args['productTitle']
        return ProductService.findWithTitle(_productTitle)

    def post(self):
        return {}, 201