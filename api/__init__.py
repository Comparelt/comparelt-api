import configparser
from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

from api.user import User

config = configparser.ConfigParser()
config.read('../config.ini')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config['DEFAULT']['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

api = Api(app, version='0.1', title="Comparelt's API Server")

api.add_namespace(User)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)