import pytest
from sqlalchemy import create_engine, inspect
from rest_api.app import models, create_db

def test_create_tables_function(tmp_path, monkeypatch):
    # Create a temporary SQLite database
    db_path = tmp_path / "test.db"
    db_url = f"sqlite:///{db_path}"

    # Patch engine and Base
    engine = create_engine(db_url)
    monkeypatch.setattr(create_db, "engine", engine)
    monkeypatch.setattr(create_db, "Base", models.Base)

    # Call the function directly
    create_db.create_tables()

    # Check if "users" table is created
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    assert "users" in tables
