"""
crud.py

Provides basic CRUD operations for the 'users' table using SQLAlchemy.

Functions:
    - insert_user(db, name, email): Inserts a new user with the given name and email.
    - search_users(db, keyword, skip=0, limit=10): Searches users by name or email,
      supports pagination.
    - update_user_email(db, user_id, new_email):
      Updates the email address of a user by user ID.
    - get_all_users(db): Retrieves all users from the database.

All functions expect an active SQLAlchemy database session as the first argument.
"""

from sqlalchemy import text


def insert_user(db, name, email):
    db.execute(text("INSERT INTO users (name, email) VALUES (:name, :email)"),
               {"name": name, "email": email})
    db.commit()


def search_users(db, keyword, skip: int = 0, limit: int = 10):
    query = text("""
        SELECT * FROM users
        WHERE name LIKE :kw OR email LIKE :kw
        LIMIT :limit OFFSET :skip
    """)
    params = {
        "kw": f"%{keyword}%",
        "limit": limit,
        "skip": skip,
    }
    return db.execute(query, params).mappings().all()


def update_user_email(db, user_id, new_email):
    query = text("UPDATE users SET email = :email WHERE id = :id")
    db.execute(query, {"email": new_email, "id": user_id})
    db.commit()


def get_all_users(db):
    return db.execute(text("SELECT * FROM users")).mappings().all()
