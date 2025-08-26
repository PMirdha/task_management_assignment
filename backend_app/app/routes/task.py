from fastapi import APIRouter, HTTPException, Depends, status
from app.routes.init_handler import get_task_business
from app.utils.jwt import verify_token
from app.models.task import Task
from app.business.task.task_business import TaskBusiness
from app.contracts import TaskCreate, TaskUpdate, TaskStatusUpdate
from app.constants import TaskStatus

router = APIRouter()


def get_current_user(token: str = Depends(lambda: None)):
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing token"
        )
    payload = verify_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )
    return payload


@router.post("/", response_model=Task)
async def create_task(
    data: TaskCreate,
    business: TaskBusiness = Depends(get_task_business),
    user=Depends(get_current_user),
):
    return await business.create_task(data)


@router.get("/", response_model=list[Task])
async def get_tasks(business: TaskBusiness = Depends(get_task_business)):
    return await business.get_tasks()


@router.get("/{task_id}", response_model=Task)
async def get_task(task_id: str, business: TaskBusiness = Depends(get_task_business)):
    task = await business.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


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


@router.delete("/{task_id}")
async def delete_task(
    task_id: str,
    business: TaskBusiness = Depends(get_task_business),
    user=Depends(get_current_user),
):
    deleted = await business.delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted"}
