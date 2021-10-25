import configparser
import os
import sqlite3
from contextlib import closing

from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

from api.auth.controller import Auth
from api.user.controller import User
from api.crawling.controller import Crawl
from api.product.controller import Product

DATABASE = '/tmp/test.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

basedir = os.path.dirname(os.path.abspath(__file__))  # To Solve Directory Issue
os.chdir(basedir)

config = configparser.ConfigParser()
config.read('../config.ini')

app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db_test:
        with app.open_resource('test.sql') as f:
            db_test.cursor().executescript(f.read().decode('utf-8'))
        db_test.commit()


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