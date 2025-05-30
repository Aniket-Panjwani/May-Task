"""
database.py

Configures the SQLAlchemy engine and session for MySQL database access.

- Loads database connection settings from environment variables (with Docker defaults).
- Constructs the DATABASE_URL for SQLAlchemy using pymysql.
- Provides:
    - engine: SQLAlchemy engine instance for database connections.
    - SessionLocal: Factory for creating new SQLAlchemy session objects.

Usage:
    Import engine and SessionLocal to interact with the database in other modules.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

import os

load_dotenv()

# Read database config from environment variables (set in docker-compose.yml)
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")  # Should be 'db' in Docker
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "mydb")

DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
