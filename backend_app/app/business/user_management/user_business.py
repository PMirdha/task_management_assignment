from passlib.context import CryptContext

from app.business.user_management.user_business_interface import IUserBusiness
from app.business.user_management.user_repository_interface import IUserRepository


class UserBusiness(IUserBusiness):
    def __init__(self, repo: IUserRepository):
        self.repo = repo
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def register_user(self, email: str, password: str):
        existing = await self.repo.find_by_email(email)
        if existing:
            return None, "Email already registered"
        hashed_pw = self.pwd_context.hash(password)
        new_user = {"email": email, "password": hashed_pw, "role": "user"}
        user_id = await self.repo.create(new_user)
        return {"id": user_id, "email": email}, None

    async def authenticate_user(self, email: str, password: str):
        db_user = await self.repo.find_by_email(email)
        if not db_user or not self.pwd_context.verify(password, db_user["password"]):
            return None
        return db_user
