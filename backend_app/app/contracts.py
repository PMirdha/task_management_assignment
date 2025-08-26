from pydantic import BaseModel, EmailStr
from app.constants import TaskStatus


class ProjectCreate(BaseModel):
    name: str
    description: str


class ProjectUpdate(BaseModel):
    name: str | None = None
    description: str | None = None


class TaskCreate(BaseModel):
    project_id: str
    title: str
    status: TaskStatus


class TaskUpdate(BaseModel):
    title: str | None = None
    status: TaskStatus | None = None


class TaskStatusUpdate(BaseModel):
    status: TaskStatus


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserRegister(BaseModel):
    email: EmailStr
    password: str
