from flask import Flask
from flask_migrate import Migrate
from app.db import db
import os
import dotenv
from app.routes.auth import auth_routes
from app.routes.task import task_routes
from flask_cors import CORS

migrate = Migrate()
dotenv.load_dotenv()

def create_app():
    """Initialization"""
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    db.init_app(app)
    migrate.init_app(db=db, app=app)

    with app.app_context():
        db.create_all()
    app.register_blueprint(auth_routes)
    app.register_blueprint(task_routes)
    return app

