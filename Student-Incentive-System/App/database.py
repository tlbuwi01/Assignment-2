from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db= SQLAlchemy()

def get_migrate(app):
    return Migrate(app, db)
