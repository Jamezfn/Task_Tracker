from flask import Flask
from flask_migrate import Migrate
from app.db import db
import os
import dotenv

migrate = Migrate()
dotenv.load_dotenv()

def create_app():
    """Initialization"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    db.init_app(app)
    migrate.init_app(db=db, app=app)
    return app