import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    SECRET_KEY: str = os.getenv('SECRET_KEY')
    DATABASE_URL: str = os.getenv('DATABASE_URL')
    DEBUG: str = os.getenv('DEBUG')

settings = Settings()