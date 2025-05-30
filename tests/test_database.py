import os
import pytest
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

# Patch environment variables for testing
os.environ["DB_USER"] = "testuser"
os.environ["DB_PASSWORD"] = "testpass"
os.environ["DB_HOST"] = "localhost"
os.environ["DB_PORT"] = "3306"
os.environ["DB_NAME"] = "testdb"

def test_database_engine_and_sessionlocal(monkeypatch):
    # Use SQLite in-memory for testing
    monkeypatch.setenv("DB_USER", "")
    monkeypatch.setenv("DB_PASSWORD", "")
    monkeypatch.setenv("DB_HOST", "")
    monkeypatch.setenv("DB_PORT", "")
    monkeypatch.setenv("DB_NAME", "")

    # Patch DATABASE_URL to use SQLite
    monkeypatch.setenv("DATABASE_URL", "sqlite:///:memory:")

    from rest_api.app import database

    # Check engine is an instance of Engine
    assert isinstance(database.engine, Engine)

    # Check SessionLocal is a sessionmaker
    assert isinstance(database.SessionLocal, sessionmaker)

    # Test creating a session
    session = database.SessionLocal()
    assert session is not None
    session.close()