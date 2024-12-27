from flask import Flask
from flask_migrate import Migrate
from app.db import db
import os
import dotenv
from app.routes.auth import auth_routes

migrate = Migrate()
dotenv.load_dotenv()

def create_app():
    """Initialization"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    db.init_app(app)
    migrate.init_app(db=db, app=app)

    with app.app_context():
        db.create_all()
    app.register_blueprint(auth_routes)
    return app

