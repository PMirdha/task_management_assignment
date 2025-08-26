from fastapi import FastAPI
from app.routes import user, project, task

app = FastAPI()
app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(project.router, prefix="/project", tags=["Project"])
app.include_router(task.router, prefix="/task", tags=["Task"])
