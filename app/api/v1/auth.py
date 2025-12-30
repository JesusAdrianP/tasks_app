from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

from app.schemas.auth import LoginRequest, TokenResponse
from app.services.auth_service import authenticate_user
from app.core.auth import create_access_token
from app.db.dependencies import get_db

router = APIRouter()

#endpoint for user login
@router.post("/login", response_model=TokenResponse, status_code=status.HTTP_200_OK)
def login_user(payload: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    user = authenticate_user(db, payload.username, payload.password)
    
    if not user:
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"message":"Invalid credentials"})
    
    token = create_access_token(data={"sub": user.email})
    
    return {"access_token": token, "token_type":"bearer"}