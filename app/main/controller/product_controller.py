from flask_restx import Resource

from ..service.product_service import ProductService
from ..util.dto import ProductDto

api = ProductDto.api
product = ProductDto.product


@api.route('/all')
class AllProduct(Resource):
    @api.doc('Get all product')
    def get(self):
        return ProductService.loadProduct(), 200


@api.route('/duplicated/<string:product_title>')
class ProductDuplicated(Resource):
    @api.doc(response={200: 'OK'})
    @api.doc(response={400: 'BAD REQUEST'})
    def get(self, product_title):
        if ProductService.findWithTitle(product_title):
            return True, 200
        else:
            return False, 200


@api.route('/<string:product_title>')
class ProductDetail(Resource):
    @api.doc(response={200: 'OK'})
    @api.doc(response={400: 'BAD REQUEST'})
    def get(self, product_title):
        return ProductService.loadProductData(product_title), 200
