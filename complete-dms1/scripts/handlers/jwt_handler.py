from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from scripts.models.jwt_model import UserSignupRequest, Token
from scripts.utils.jwt_utils import create_user_token
from scripts.utils.mongo_utils import MongoDBConnection
from scripts.logging.logger import logger
from passlib.context import CryptContext

mongodb = MongoDBConnection()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def signup_user_handler(user: UserSignupRequest) -> Token:
    users_collection = mongodb.get_collection("users")

    existing_user = users_collection.find_one({"username": user.username})

    if existing_user:
        logger.warning(f"Signup failed: User '{user.username}' already exists")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )

    hashed_password = pwd_context.hash(user.password)

    new_user = {
        "username": user.username,
        "password": hashed_password
    }
    users_collection.insert_one(new_user)

    logger.info(f"User '{user.username}' registered successfully")

    access_token = create_user_token(user.username)
    return Token(access_token=access_token)


def login_user_handler(form_data: OAuth2PasswordRequestForm) -> Token:
    users_collection = mongodb.get_collection("users")

    username = form_data.username
    password = form_data.password

    user_record = users_collection.find_one({"username": username})

    if not user_record:
        logger.warning(f"Login failed for user '{username}' - User not found")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    if not pwd_context.verify(password, user_record["password"]):
        logger.warning(f"Login failed for user '{username}' - Incorrect password")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    logger.info(f"User '{username}' authenticated successfully")
    access_token = create_user_token(username)
    return Token(access_token=access_token)


def logout_user_handler(username: str):

    if not username:
        logger.warning("Logout failed: No username provided")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid logout request"
        )

    logger.info(f"User '{username}' logged out successfully")
    return {"message": f"User '{username}' logged out successfully"}