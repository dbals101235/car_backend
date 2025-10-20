from motor.motor_asyncio import AsyncIOMotorClient
from config import BaseConfig

config = BaseConfig()

client = AsyncIOMotorClient(config.DB_URL)
db = client[config.DB_NAME]
