from app.db import db
import bcrypt
from app.models.user import User
from flask import jsonify
import jwt
import os
import dotenv
from datetime import datetime, timedelta
from app.custom_exceptions import CustomJwtException

dotenv.load_dotenv()


class UserContoller:
    def create_user(self, name, email, password):
        user = db.session.query(User).filter_by(email=email).first()
        if user:
            return jsonify({"error": "user already exists"}), 400
        hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        db.session.add(User(name, email, password=hash))
        db.session.commit()
        return jsonify({"message": "User created succesfully"}), 200
    def login_user(self, email, password):
        user = db.session.query(User).filter_by(email=email).first()
        if not user:
            return jsonify({"error": "User not found check your email"}), 404
        if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            return jsonify({"error": "Password does not match"}), 400
        
        user_object = {
            "name": user.name,
            "email": user.email
        }
    
        exp_time = datetime.utcnow() + timedelta(hours=1)
        token = jwt.encode({"user_id": user.id, "exp": exp_time}, os.getenv("JWT_SECRET"), algorithm='HS256')
        return jsonify({"Message": "Login successful", "token": token, "user": user_object }), 200
    
    def authorise_user(self, token):
        """Authorise user"""
        try:
            user = jwt.decode(token, os.getenv("JWT_SECRET"), algorithms=['HS256'])
<<<<<<< HEAD
            return user['user_id'] # if user else None
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 400
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 400
=======
            return user['user_id'] if user else  None
        except jwt.ExpiredSignatureError:
            raise CustomJwtException("Token Expired")
        except jwt.InvalidTokenError:
            raise CustomJwtException("Invalid Token")
>>>>>>> d31cbba0647350b98fe95363fb8071a6e8c038d7

user_controller = UserContoller()