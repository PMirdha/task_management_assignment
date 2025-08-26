# Project model for MongoDB
from pydantic import BaseModel


from pydantic import BaseModel, Field


class Project(BaseModel):
    id: str
    name: str
    description: str
    creator_id: str
