from abc import ABC, abstractmethod


class ITaskBusiness(ABC):
    @abstractmethod
    async def create_task(self, data):
        pass

    @abstractmethod
    async def get_tasks(self):
        pass

    @abstractmethod
    async def get_task(self, task_id: str):
        pass

    @abstractmethod
    async def update_task_status(self, task_id: str, data):
        pass

    @abstractmethod
    async def update_task(self, task_id: str, data):
        pass

    @abstractmethod
    async def delete_task(self, task_id: str):
        pass
