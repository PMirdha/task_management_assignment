from fastapi import APIRouter, HTTPException, Depends, status
from app.routes.init_handler import get_project_business
from app.utils.jwt import verify_token
from app.models.project import Project
from app.contracts import ProjectCreate, ProjectUpdate
from app.business.project.project_business import ProjectBusiness

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


@router.post("/", response_model=Project)
async def create_project(
    data: ProjectCreate,
    business: ProjectBusiness = Depends(get_project_business),
    user=Depends(get_current_user),
):
    project = await business.create_project(data, user["sub"])
    return project


@router.get("/", response_model=list[Project])
async def get_projects(business: ProjectBusiness = Depends(get_project_business)):
    return await business.get_projects()


@router.get("/{project_id}", response_model=Project)
async def get_project(
    project_id: str, business: ProjectBusiness = Depends(get_project_business)
):
    project = await business.get_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.put("/{project_id}", response_model=Project)
async def update_project(
    project_id: str,
    data: ProjectUpdate,
    business: ProjectBusiness = Depends(get_project_business),
    user=Depends(get_current_user),
):
    updated_project, error = await business.update_project(
        project_id, data, user["sub"]
    )
    if error == "not_found":
        raise HTTPException(status_code=404, detail="Project not found")
    if error == "forbidden":
        raise HTTPException(status_code=403, detail="Not authorized")
    return updated_project


@router.delete("/{project_id}")
async def delete_project(
    project_id: str,
    business: ProjectBusiness = Depends(get_project_business),
    user=Depends(get_current_user),
):
    _, error = await business.delete_project(project_id, user["sub"])
    if error == "not_found":
        raise HTTPException(status_code=404, detail="Project not found")
    if error == "forbidden":
        raise HTTPException(status_code=403, detail="Only creator can delete project")
    return {"detail": "Project deleted"}
