from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from rest_api.app.models import Base, User

def test_user_model_table_creation():
    # Use in-memory SQLite database for testing
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    assert "users" in tables

def test_user_model_columns():
    # Check User model columns and constraints
    columns = User.__table__.columns
    assert "id" in columns
    assert "name" in columns
    assert "email" in columns
    assert "created_at" in columns

    assert columns["id"].primary_key
    assert columns["name"].nullable is False
    assert columns["email"].unique is True