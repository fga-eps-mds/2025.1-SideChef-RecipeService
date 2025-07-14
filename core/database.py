from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()


client = MongoClient(os.getenv("ME_CONFIG_MONGODB_URL"))
db = client[os.getenv("MONGO_DB_NAME")]