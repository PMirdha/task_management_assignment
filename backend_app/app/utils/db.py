# MongoDB connection utility
from motor.motor_asyncio import AsyncIOMotorClient
from app.config import get_config

config = get_config()
client = AsyncIOMotorClient(config.mongo_url)
db = client[config.mongo_db]


def get_db():
    return db
