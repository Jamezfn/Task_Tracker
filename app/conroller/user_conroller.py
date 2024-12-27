from app.db import db
from app.models.user import User

class UserContoller:
    def create_user(self, name, email, password):
        db.session.add(User(name, email, password))
        db.session.commit()

    def authenticate_user(self, email, password):
        pass

user_controller = UserContoller()