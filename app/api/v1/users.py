from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserOut
from app.services.user_service import create_user, get_user_by_email, get_user_by_username
from app.db.dependencies import get_db

router = APIRouter()

#Endpoint to register a new user
@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register_user(payload: UserCreate, db: Session = Depends(get_db)):
    #verify if user with email or username already exists
    existing_user = get_user_by_email(db, payload.email)
    if existing_user:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message":"Email already registered"})
    existing_user = get_user_by_username(db, payload.username)
    if existing_user:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message":"Username already taken"})
    
    new_user = create_user(db, payload.username, payload.email, payload.password)
    return new_user