from abc import ABC, abstractmethod


class IUserRepository(ABC):
    @abstractmethod
    async def find_by_email(self, email: str) -> dict:
        pass

    @abstractmethod
    async def create(self, user_data: dict) -> str:
        pass
