from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest

from rest_api.app.main import app, get_db
from rest_api.app.models import Base

# Use an in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables once for all tests
Base.metadata.create_all(bind=engine)

# Dependency override
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"name": "TestUser", "email": "testuser@example.com"})
    assert response.status_code == 200
    assert response.json() == {"message": "User created"}

def test_search_users():
    # Ensure user exists
    client.post("/users/", json={"name": "SearchUser", "email": "searchuser@example.com"})
    response = client.get("/users/", params={"keyword": "SearchUser"})
    assert response.status_code == 200
    assert any(user["name"] == "SearchUser" for user in response.json())

def test_get_all_users():
    # Ensure at least one user exists
    client.post("/users/", json={"name": "AllUser", "email": "alluser@example.com"})
    response = client.get("/users/all")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert any(user["name"] == "AllUser" for user in response.json())

def test_update_user_email():
    # Create user
    client.post("/users/", json={"name": "UpdateUser", "email": "updateuser@example.com"})
    users = client.get("/users/", params={"keyword": "UpdateUser"}).json()
    user_id = users[0]["id"]
    response = client.put(f"/users/{user_id}", json={"new_email": "updateduser@example.com"})
    assert response.status_code == 200
    assert response.json() == {"message": "Email updated"}
    updated_users = client.get("/users/", params={"keyword": "updateduser@example.com"}).json()
    assert any(user["email"] == "updateduser@example.com" for user in updated_users)