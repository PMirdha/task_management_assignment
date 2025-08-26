from typing import List, Optional
from bson import ObjectId
from app.models.task import Task
from app.constants import TaskStatus
from app.business.task.task_repository_interface import ITaskRepository


class TaskRepository(ITaskRepository):
    def __init__(self, db):
        self.collection = db["tasks"]

    async def create(self, data: dict) -> Task:
        # Ensure status is stored as string value
        if "status" in data and isinstance(data["status"], TaskStatus):
            data["status"] = data["status"].value
        result = await self.collection.insert_one(data)
        data["id"] = str(result.inserted_id)
        return Task(**data)

    async def get_all(self) -> List[Task]:
        tasks = []
        async for t in self.collection.find():
            t["id"] = str(t["_id"])
            tasks.append(Task(**t))
        return tasks

    async def get_by_id(self, task_id: str) -> Optional[Task]:
        t = await self.collection.find_one({"_id": ObjectId(task_id)})
        if not t:
            return None
        t["id"] = str(t["_id"])
        return Task(**t)

    async def update(self, task_id: str, update_data: dict) -> Optional[Task]:
        # Ensure status is stored as string value
        if "status" in update_data and isinstance(update_data["status"], TaskStatus):
            update_data["status"] = update_data["status"].value
        t = await self.collection.find_one({"_id": ObjectId(task_id)})
        if not t:
            return None
        await self.collection.update_one(
            {"_id": ObjectId(task_id)}, {"$set": update_data}
        )
        t.update(update_data)
        t["id"] = str(t["_id"])
        return Task(**t)

    async def delete(self, task_id: str) -> bool:
        result = await self.collection.delete_one({"_id": ObjectId(task_id)})
        return result.deleted_count == 1
