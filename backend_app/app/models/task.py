# Task model for MongoDB
from pydantic import BaseModel


from pydantic import BaseModel, Field
from app.constants import TaskStatus


class Task(BaseModel):
    id: str
    project_id: str
    title: str
    status: TaskStatus
