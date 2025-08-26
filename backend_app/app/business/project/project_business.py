from app.contracts import ProjectCreate, ProjectUpdate
from app.business.project.project_business_interface import IProjectBusiness
from app.business.project.project_repository_interface import IProjectRepository


class ProjectBusiness(IProjectBusiness):
    def __init__(self, repo: IProjectRepository):
        self.repo = repo

    async def create_project(self, data: ProjectCreate, user_id: str):
        project_data = {
            "name": data.name,
            "description": data.description,
            "creator_id": user_id,
        }
        return await self.repo.create(project_data)

    async def get_projects(self):
        return await self.repo.get_all()

    async def get_project(self, project_id: str):
        return await self.repo.get_by_id(project_id)

    async def update_project(self, project_id: str, data: ProjectUpdate, user_id: str):
        project = await self.repo.get_by_id(project_id)
        if not project:
            return None, "not_found"
        if project.creator_id != user_id:
            return None, "forbidden"
        update_data = {k: v for k, v in data.dict().items() if v is not None}
        updated_project = await self.repo.update(project_id, update_data)
        return updated_project, None

    async def delete_project(self, project_id: str, user_id: str):
        project = await self.repo.get_by_id(project_id)
        if not project:
            return False, "not_found"
        if project.creator_id != user_id:
            return False, "forbidden"
        deleted = await self.repo.delete(project_id)
        if not deleted:
            return False, "not_found"
        return True, None
