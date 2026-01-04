# config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")          # Get secret key from .env
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")  # Database connection
    SQLALCHEMY_TRACK_MODIFICATIONS = False       # Avoid extra memory usage
    DEBUG = os.getenv("DEBUG", "False") == "True"  # Convert string to boolean
