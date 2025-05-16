from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os
from dotenv import load_dotenv

load_dotenv()

def get_db():
    try:
        client = MongoClient(os.getenv("MONGODB_URI"))
        db = client["RecipeService"]
        return db
    except ConnectionFailure:
        print("Database connection Error")
        return None