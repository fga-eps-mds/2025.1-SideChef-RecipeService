from pymongo import MongoClient
from core.config_loader import settings

client = MongoClient(settings.MONGO_URL)
db = client[settings.DB_NAME]