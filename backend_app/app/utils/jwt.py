# JWT utility functions
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from app.config import get_config

config = get_config()
SECRET_KEY = config.jwt_secret
ALGORITHM = config.jwt_algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = config.access_token_expire_minutes


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
