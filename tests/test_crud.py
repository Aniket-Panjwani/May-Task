import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from rest_api.app import models, crud
from rest_api.app.database import Base

@pytest.fixture(scope="module")
def db():
    engine = create_engine("sqlite:///:memory:")
    testing_session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    db = testing_session_local()
    yield db
    db.close()

def test_insert_and_search_user(db):
    crud.insert_user(db, "Alice", "alice@example.com")
    users = crud.search_users(db, "Alice")
    assert users
    assert users[0]["name"] == "Alice"

def test_update_user_email(db):
    crud.insert_user(db, "Bob", "bob@example.com")
    user = crud.search_users(db, "Bob")[0]
    crud.update_user_email(db, user["id"], "bob2@example.com")
    updated = crud.search_users(db, "bob2@example.com")
    assert updated[0]["email"] == "bob2@example.com"