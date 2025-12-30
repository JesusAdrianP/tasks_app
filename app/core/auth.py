from datetime import datetime, timedelta, timezone
from jose import jwt
from app.core.config import settings

#function to create access token
def create_access_token(data:dict, expires_delta: timedelta | None = None):
    encode = data.copy()
    expires = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    encode.update({"exp": expires})
    encoded_jwt = jwt.encode(encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt