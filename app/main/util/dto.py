from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email', example='dku@example.com'),
        'password': fields.String(required=True, description='user password', example="dku@2020"),
        'username': fields.String(required=True, description='username', example="dku"),
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='User Email', example='dku@example.com'),
        'password': fields.String(required=True, description='User password ', example='dku@2020'),
    })


class ProductDto:
    api = Namespace('product', description='product related operations')
    product = api.model('product', {
        'title': fields.String(required=True, description='Product Title', example='dku'),
        'picture': fields.String(required=True, description='Product picture', example='images/2115136326'),
        'link': fields.String(required=True, description='Product Link', example='dku@example.com'),
        'price': fields.String(required=True, description='Product Price', example='$200')
    })


class CrawlingDto:
    api = Namespace('crawling', description='crawling product related operations')
    crawling = ProductDto.product
