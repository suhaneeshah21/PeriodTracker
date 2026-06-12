from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "NariHealth API"
    DEBUG: bool = True
    FIREBASE_CREDENTIALS_PATH: str = "firebase-credentials.json"
    
    class Config:
        env_file = ".env"

settings = Settings()