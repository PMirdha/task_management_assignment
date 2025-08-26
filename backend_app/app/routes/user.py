from fastapi import APIRouter, HTTPException, Depends
from app.business.user_management.user_business import UserBusiness
from app.contracts import UserLogin, UserRegister
from app.routes.init_handler import get_user_business
from app.utils.jwt import create_access_token

router = APIRouter()


@router.post("/register")
async def register(
    user: UserRegister,
    business: UserBusiness = Depends(get_user_business),
):
    result, error = await business.register_user(user.email, user.password)
    if error:
        raise HTTPException(status_code=400, detail=error)
    return result


@router.post("/login")
async def login(
    user: UserLogin,
    business: UserBusiness = Depends(get_user_business),
):
    db_user = await business.authenticate_user(user.email, user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": str(db_user["_id"]), "role": db_user["role"]})
    return {"access_token": token, "token_type": "bearer"}
