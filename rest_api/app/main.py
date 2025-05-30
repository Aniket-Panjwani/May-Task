"""
main.py

FastAPI application for managing users.

Endpoints:
    - POST /users/: Create a new user with name and email.
    - GET /users/: Search users by keyword (name or email), with pagination.
    - GET /users/all: Retrieve all users from the database.
    - PUT /users/{user_id}: Update the email address of a user by user ID.

Dependencies:
    - Uses SQLAlchemy session from app.database.
    - CRUD operations are handled by app.crud.
    - Uses Pydantic models for request validation.
"""

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from app.database import SessionLocal
from app import crud

app = FastAPI()


# Pydantic model for creating a user
class UserCreate(BaseModel):
    name: str
    email: str


# Pydantic model for updating user email
class UserUpdateEmail(BaseModel):
    new_email: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/")
def create_user(user: UserCreate, db=Depends(get_db)):
    crud.insert_user(db, user.name, user.email)
    return {"message": "User created"}


@app.get("/users/")
def search_users(keyword: str, skip: int = 0, limit: int = 10, db=Depends(get_db)):
    results = crud.search_users(db, keyword, skip, limit)
    return results


@app.get("/users/all")
def get_all_users(db=Depends(get_db)):
    results = crud.get_all_users(db)
    return [dict(row) for row in results]


@app.put("/users/{user_id}")
def update_email(user_id: int, email_update: UserUpdateEmail, db=Depends(get_db)):
    crud.update_user_email(db, user_id, email_update.new_email)
    return {"message": "Email updated"}
