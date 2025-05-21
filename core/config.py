import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MONGO_URL = os.getenv("ME_CONFIG_MONGODB_URL")
    DB_NAME = "RecipeService"
    FRONTEND_CORS_ORIGINS = os.getenv("FRONTEND_CORS_ORIGINS")