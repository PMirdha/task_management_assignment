from typing import Optional
from fastapi import APIRouter, HTTPException, Depends
from app.routes.init_handler import get_task_business
from app.utils.auth import get_current_user
from app.models.task import Task
from app.business.task.task_business import TaskBusiness
from app.contracts import TaskCreate, TaskUpdate, TaskStatusUpdate

router = APIRouter()


@router.post("/", response_model=Optional[Task])
async def create_task(
    data: TaskCreate,
    business: TaskBusiness = Depends(get_task_business),
    user=Depends(get_current_user),
):
    task, error = await business.create_task(data)
    if error:
        raise HTTPException(status_code=400, detail=error)
    return task


@router.get("/", response_model=list[Task])
async def get_tasks(
    business: TaskBusiness = Depends(get_task_business), user=Depends(get_current_user)
):
    return await business.get_tasks()


@router.patch("/{task_id}/status", response_model=Task)
async def update_task_status(
    task_id: str,
    data: TaskStatusUpdate,
    business: TaskBusiness = Depends(get_task_business),
    user=Depends(get_current_user),
):
    updated_task = await business.update_task_status(task_id, data)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task


@router.put("/{task_id}", response_model=Task)
async def update_task(
    task_id: str,
    data: TaskUpdate,
    business: TaskBusiness = Depends(get_task_business),
    user=Depends(get_current_user),
):
    updated_task = await business.update_task(task_id, data)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task
