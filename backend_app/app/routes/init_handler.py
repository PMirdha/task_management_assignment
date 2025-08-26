from app.business.project.project_business import ProjectBusiness
from app.business.task.task_business import TaskBusiness
from app.business.user_management.user_business import UserBusiness
from app.repositories.project_repository import ProjectRepository
from app.repositories.task_repository import TaskRepository
from app.repositories.user_repository import UserRepository
from app.utils.db import get_db


from fastapi import Depends


def get_user_business(db=Depends(get_db)):
    repo = UserRepository(db)
    return UserBusiness(repo)


def get_task_business(db=Depends(get_db)):
    repo = ProjectRepository(db)
    project_business = ProjectBusiness(repo)
    repo = TaskRepository(db)
    return TaskBusiness(repo, project_business)


def get_project_business(db=Depends(get_db)):
    repo = ProjectRepository(db)
    return ProjectBusiness(repo)
