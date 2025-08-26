from typing import Optional
from app.business.user_management.user_repository_interface import IUserRepository


class UserRepository(IUserRepository):
    def __init__(self, db):
        self.collection = db["users"]

    async def find_by_email(self, email: str) -> Optional[dict]:
        return await self.collection.find_one({"email": email})

    async def create(self, user_data: dict) -> str:
        result = await self.collection.insert_one(user_data)
        return str(result.inserted_id)
