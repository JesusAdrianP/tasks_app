from pydantic import BaseModel, EmailStr

#Validation schema for user creation
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

#validation for user output
class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool
    
    model_config = {
        "from_attributes": True
    }