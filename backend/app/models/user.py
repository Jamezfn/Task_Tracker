from app.db import db
from sqlalchemy.orm import Mapped, mapped_column
import uuid

class User(db.Model):
    __tablename__ = 'users'
    id: Mapped[str] = mapped_column(db.String(255), default=uuid.uuid4(), primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    email: Mapped[str] = mapped_column(db.String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String(255), nullable=False)
    tasks: Mapped[str] = db.relationship("Task", backref="user")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password