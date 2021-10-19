from flask_migrate import Migrate
from api.app import app, db
from api.user import models

migrate = Migrate(app, db)