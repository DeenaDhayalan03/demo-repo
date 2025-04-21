from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from scripts.models.jwt_model import UserSignupRequest, Token
from scripts.handlers.jwt_handler import signup_user_handler, login_user_handler, logout_user_handler
from scripts.constants.api_endpoints import Endpoints
from fastapi.security import OAuth2PasswordBearer
from scripts.utils.jwt_utils import decode_access_token
from scripts.logging.logger import logger

authentication_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login/")


def get_current_user(token: str = Depends(oauth2_scheme)):
    username = decode_access_token(token)
    if not username:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return username

@authentication_router.post(Endpoints.AUTH_SIGNUP, response_model=Token, status_code=status.HTTP_201_CREATED)
def signup_view(user: UserSignupRequest):

    logger.info(f"Attempting signup for user: {user.username}")
    result = signup_user_handler(user)
    logger.info(f"User '{user.username}' signed up successfully")
    return result

@authentication_router.post(Endpoints.AUTH_LOGIN, response_model=Token)
def login_view(form_data: OAuth2PasswordRequestForm = Depends()):

    logger.info(f"User '{form_data.username}' attempting login")
    result = login_user_handler(form_data)
    logger.info(f"User '{form_data.username}' logged in successfully")
    return result

@authentication_router.post(Endpoints.AUTH_LOGOUT, status_code=status.HTTP_200_OK)
def logout_view(username: str = Depends(get_current_user)):
    logger.info(f"User '{username}' attempting logout")
    result = logout_user_handler(username)
    logger.info(f"User '{username}' logged out successfully")
    return result