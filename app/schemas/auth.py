from pydantic import BaseModel

#Request schema for user login
class LoginRequest(BaseModel):
    email:str
    password:str

#Response schema for token
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"