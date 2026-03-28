import motor.motor_asyncio 
from app.config import settings

client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_url)
db = client[settings.database_name]

user_collection = db["users"]
products_collection = db["products"]