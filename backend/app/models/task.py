from app.db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Date
from sqlalchemy import Enum
import uuid

class Task(db.Model):
    __tablename__ = "tasks"
    id: Mapped[str] = mapped_column(db.String(255), primary_key=True)
    title: Mapped[str] = mapped_column(db.String(255), nullable=False)
    description: Mapped[str] = mapped_column(db.String(255))
    status: Mapped[str] = mapped_column(db.String(255), Enum("Pending", "In Progress", "Completed", name="status_enum"), nullable=False, default="Pending")
    start_date: Mapped[Date] = mapped_column(Date, nullable=False)
    due_date: Mapped[Date] = mapped_column(Date, nullable=False)
    user_id: Mapped[str] = mapped_column(db.String(255), db.ForeignKey("users.id"))

    def __init__(self, title, description, status, start_date, due_date, user_id):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.status = status
        self.start_date = start_date
        self.due_date = due_date
        self.user_id = user_id