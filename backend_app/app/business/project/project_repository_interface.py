from abc import ABC, abstractmethod


class IProjectRepository(ABC):
    @abstractmethod
    async def create(self, data: dict):
        pass

    @abstractmethod
    async def get_all(self):
        pass

    @abstractmethod
    async def get_by_id(self, project_id: str):
        pass

    @abstractmethod
    async def update(self, project_id: str, update_data: dict):
        pass

    @abstractmethod
    async def delete(self, project_id: str):
        pass
