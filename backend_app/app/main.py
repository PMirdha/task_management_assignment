from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from app.config import AppConfig, get_config
from app.routes import user, project, task


def init_middleware(app: FastAPI, settings: AppConfig):
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=settings.allowed_hosts,
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


app = FastAPI()
init_middleware(app, get_config())
app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(project.router, prefix="/project", tags=["Project"])
app.include_router(task.router, prefix="/task", tags=["Task"])
