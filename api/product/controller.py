from flask_restx import Namespace, Resource, reqparse, fields
from api.product.service import *

Product = Namespace(name="Product", description="Product API")

product_fields = Product.inherit('Get Product', {
    'productTitle': fields.String(description='Product Title', required=True, example="DKU")
})


@Product.route('')
class Products(Resource):
    @Product.expect(product_fields)
    @Product.doc(response={200:'OK'})
    @Product.doc(response={400:'BAD REQUEST'})
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('productTitle', type=str)
        args = parser.parse_args()

        _productTitle = args['productTitle']
        return ProductService.findWithTitle(_productTitle)

    def post(self):
        return {}, 201