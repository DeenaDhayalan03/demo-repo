from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.models.user import UserCreate, Token
from app.handlers.jwt_handler import signup_user, login_user

router = APIRouter()

@router.post("/auth/signup/")
def signup(user: UserCreate):
    return signup_user(user)

@router.post("/auth/login/", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return login_user(form_data)
