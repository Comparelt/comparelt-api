from flask_restx import Api
from flask import Blueprint

from .main.controller.auth_controller import api as auth_api
from .main.controller.user_controller import api as user_api
from .main.controller.product_controller import api as product_api
from .main.controller.crawling_controller import api as crawl_api

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='Flask REST Comparelt API  with JWT Token',
    version='0.1',
    description='Comparelt flask Rest API',
)

api.add_namespace(auth_api, path='/auth')
api.add_namespace(user_api, path='/user')
api.add_namespace(product_api, path='/product')
api.add_namespace(crawl_api, path='/crawl')
