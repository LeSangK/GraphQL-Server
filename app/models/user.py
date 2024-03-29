# app/models/user.py

from sqlalchemy import Column, Integer, String
from app.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), unique=True, nullable=False)
