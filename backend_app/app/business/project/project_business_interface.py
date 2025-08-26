from abc import ABC, abstractmethod


class IProjectBusiness(ABC):
    @abstractmethod
    async def create_project(self, data, user_id: str):
        pass

    @abstractmethod
    async def get_projects(self):
        pass

    @abstractmethod
    async def get_project(self, project_id: str):
        pass

    @abstractmethod
    async def update_project(self, project_id: str, data, user_id: str):
        pass

    @abstractmethod
    async def delete_project(self, project_id: str, user_id: str):
        pass
