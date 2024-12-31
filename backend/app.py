from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from app.routes.auth import auth_routes

app = Flask(__name__)
# initiallizing database
load_dotenv()
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(app, model_class=Base)

class User(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(db.String(255), unique=False, nullable=False)

with app.app_context():
    db.create_all()
    try:
        db.session.add(User(username="Example"))
        db.session.commit()
    except Exception as e:
        print(e)
    users = db.session.execute(db.select(User)).scalars()
    for user in users:
        print(f"{user.id} named {user.username}")
    
@app.route('/')
def hello_world():
    return "<p>Hello, World welcome!</p>"

app.register_blueprint(auth_routes)

if __name__ == "__main__":
    app.run(debug=True)