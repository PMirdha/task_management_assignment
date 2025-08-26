from typing import List, Optional
from bson import ObjectId
from app.models.project import Project
from app.business.project.project_repository_interface import IProjectRepository


class ProjectRepository(IProjectRepository):
    def __init__(self, db):
        self.collection = db["projects"]

    async def create(self, data: dict) -> Project:
        result = await self.collection.insert_one(data)
        data["id"] = str(result.inserted_id)
        return Project(**data)

    async def get_all(self) -> List[Project]:
        projects = []
        async for p in self.collection.find():
            p["id"] = str(p["_id"])
            projects.append(Project(**p))
        return projects

    async def get_by_id(self, project_id: str) -> Optional[Project]:
        p = await self.collection.find_one({"_id": ObjectId(project_id)})
        if not p:
            return None
        p["id"] = str(p["_id"])
        return Project(**p)

    async def update(self, project_id: str, update_data: dict) -> Optional[Project]:
        p = await self.collection.find_one({"_id": ObjectId(project_id)})
        if not p:
            return None
        await self.collection.update_one(
            {"_id": ObjectId(project_id)}, {"$set": update_data}
        )
        p.update(update_data)
        p["id"] = str(p["_id"])
        return Project(**p)

    async def delete(self, project_id: str) -> bool:
        result = await self.collection.delete_one({"_id": ObjectId(project_id)})
        return result.deleted_count == 1
