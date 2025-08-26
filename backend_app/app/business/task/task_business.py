from app.contracts import TaskCreate, TaskUpdate, TaskStatusUpdate
from app.constants import TaskStatus
from app.business.task.task_business_interface import ITaskBusiness
from app.business.task.task_repository_interface import ITaskRepository


class TaskBusiness(ITaskBusiness):
    def __init__(self, repo: ITaskRepository):
        self.repo = repo

    async def create_task(self, data: TaskCreate):
        task_data = {
            "project_id": data.project_id,
            "title": data.title,
            "status": data.status,
        }
        return await self.repo.create(task_data)

    async def get_tasks(self):
        return await self.repo.get_all()

    async def get_task(self, task_id: str):
        return await self.repo.get_by_id(task_id)

    async def update_task_status(self, task_id: str, data: TaskStatusUpdate):
        task = await self.repo.get_by_id(task_id)
        if not task:
            return None
        return await self.repo.update(task_id, {"status": data.status.value})

    async def update_task(self, task_id: str, data: TaskUpdate):
        task = await self.repo.get_by_id(task_id)
        if not task:
            return None
        update_data = {
            k: (v.value if isinstance(v, TaskStatus) else v)
            for k, v in data.dict().items()
            if v is not None
        }
        return await self.repo.update(task_id, update_data)

    async def delete_task(self, task_id: str):
        task = await self.repo.get_by_id(task_id)
        if not task:
            return False
        return await self.repo.delete(task_id)
