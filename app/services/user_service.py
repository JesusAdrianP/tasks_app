from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password

#service for creating a new user
def create_user(db:Session, username:str, email:str, password:str):
    user = User(
        username=username,
        email=email,
        hashed_password=hash_password(password),
        is_active=True
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

#service for getting a user by email
def get_user_by_email(db:Session, email:str):
    return db.query(User).filter(User.email == email).first()

#service for getting a user by username
def get_user_by_username(db:Session, username:str):
    return db.query(User).filter(User.username == username).first()