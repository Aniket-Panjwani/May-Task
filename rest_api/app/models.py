"""
models.py

Defines SQLAlchemy ORM models for the application.

Classes:
    - User: Represents a user record in the 'users' table with fields:
        - id: Primary key, integer.
        - name: User's name, string, not nullable.
        - email: User's email, unique string, not nullable.
        - created_at: Timestamp of user creation.
"""

from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(TIMESTAMP)
