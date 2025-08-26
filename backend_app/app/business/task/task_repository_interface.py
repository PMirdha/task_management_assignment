from abc import ABC, abstractmethod
from typing import List, Optional
from app.models.task import Task


class ITaskRepository(ABC):
    @abstractmethod
    async def create(self, data: dict) -> Task:
        pass

    @abstractmethod
    async def get_all(self) -> List[Task]:
        pass

    @abstractmethod
    async def get_by_id(self, task_id: str) -> Optional[Task]:
        pass

    @abstractmethod
    async def update(self, task_id: str, update_data: dict) -> Optional[Task]:
        pass

    @abstractmethod
    async def delete(self, task_id: str) -> bool:
        pass
