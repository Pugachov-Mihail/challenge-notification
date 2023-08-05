from motor.motor_asyncio import AsyncIOMotorClient

from notification_api.config.settings import MONGO_DB_URL


conn = AsyncIOMotorClient(MONGO_DB_URL)

db = conn.notification