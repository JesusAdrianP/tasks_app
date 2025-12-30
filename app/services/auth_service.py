from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import verify_password

#service for user authentication
def authenticate_user(db:Session, email:str, password:str):
    user = db.query(User).filter(User.email == email).first()
    #verify if user exists, is active and password is correct
    if not user:
        return None
    if not user.is_active:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user