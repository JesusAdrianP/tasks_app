from passlib.context import CryptContext

#setting up password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#function to hash passsword using the pwd_context
def hash_password(password:str) -> str:
    return pwd_context.hash(password)

#function to verify passsword using the pwd_context
def verify_password(plain_password:str, hashed_password:str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)