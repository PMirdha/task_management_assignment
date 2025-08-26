from abc import ABC, abstractmethod


class IUserBusiness(ABC):
    @abstractmethod
    async def register_user(self, email: str, password: str):
        pass

    @abstractmethod
    async def authenticate_user(self, email: str, password: str):
        pass
