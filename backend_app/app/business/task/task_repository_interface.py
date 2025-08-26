from abc import ABC, abstractmethod


class ITaskRepository(ABC):
    @abstractmethod
    async def create(self, data: dict):
        pass

    @abstractmethod
    async def get_all(self):
        pass

    @abstractmethod
    async def get_by_id(self, task_id: str):
        pass

    @abstractmethod
    async def update(self, task_id: str, update_data: dict):
        pass

    @abstractmethod
    async def delete(self, task_id: str):
        pass
