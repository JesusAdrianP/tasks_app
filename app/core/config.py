from pydantic_settings import BaseSettings
from pydantic import ConfigDict

#Base app settings class
class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    
    model_config = ConfigDict(
        env_file=".env",
        extra="ignore",
        env_file_encoding='utf-8'
    )
        
settings = Settings()

print("Database url:", repr(settings.DATABASE_URL))