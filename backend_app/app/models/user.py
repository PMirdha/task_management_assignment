# User model for MongoDB
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: str
    email: EmailStr
    password: str
    role: str = "user"
