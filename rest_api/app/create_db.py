"""
create_db.py

Initializes the database schema by creating all tables defined in models.
py using SQLAlchemy.

- Imports the SQLAlchemy engine and Base metadata.
- Executes Base.metadata.create_all(bind=engine)to create tables if they do not exist.
- Prints a confirmation message upon successful creation.

Usage:
    Run this script to set up the database tables before starting the application.
"""

from rest_api.app.database import engine
from rest_api.app.models import Base

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Database tables created.")

if __name__ == "__main__":
    create_tables()
