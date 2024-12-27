from app.db import db
from sqlalchemy.orm import Mapped, mapped_column
import uuid

class User(db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(db.Integer, default=uuid.uuid4(), primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    email: Mapped[str] = mapped_column(db.String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String(255), nullable=False)