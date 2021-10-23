import configparser
from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

from api.user.controller import User
from api.crawling import Crawl
from api.auth.controller import Auth
from api.product.controller import Product

config = configparser.ConfigParser()
config.read('../config.ini')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config['DEFAULT']['SQLALCHEMY_DATABASE_URI']  # To Connect to DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # To avoid FSADeprecationWarning
db = SQLAlchemy(app)


api = Api(app, version='0.1', title="Comparelt's API Server")

api.add_namespace(Auth, '/auth')
api.add_namespace(User, '/user')
api.add_namespace(Crawl, '/crawl')
api.add_namespace(Product, '/product')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)