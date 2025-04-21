from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials
from scripts.constants.app_configuration import settings
from scripts.constants.app_constants import (
    UNAUTHORIZED, TOKEN_EXPIRED, INVALID_TOKEN
)
from scripts.models.jwt_model import TokenData

SECRET_KEY = settings.JWT_SECRET
ALGORITHM = settings.JWT_ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:

    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str) -> Optional[str]:

    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = decoded_token.get("sub")

        if username is None:
            raise JWTError("Token does not contain subject")

        return username
    except JWTError:
        return None


def decode_access_token(token: str) -> dict:

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail=TOKEN_EXPIRED)
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail=INVALID_TOKEN)


def get_current_user_from_token(request: Request) -> TokenData:

    credentials: HTTPAuthorizationCredentials = request.headers.get("Authorization")

    if credentials:
        if credentials.lower().startswith("bearer "):
            token = credentials.split(" ")[1]
            token_data = verify_access_token(token)

            if token_data:
                return TokenData(username=token_data)
            else:
                raise HTTPException(status_code=401, detail=INVALID_TOKEN)

    raise HTTPException(status_code=401, detail=UNAUTHORIZED)


def create_user_token(username: str) -> str:

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        "sub": username,
        "exp": expire
    }
    return create_access_token(payload)
