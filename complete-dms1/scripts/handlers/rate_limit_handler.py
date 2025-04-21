from fastapi import HTTPException, status
from scripts.utils.mongo_utils import MongoDBConnection
from scripts.models.rate_limit_model import RateLimitConfig
from scripts.logging.logger import logger

mongodb = MongoDBConnection()

def get_rate_limit_handler(user_id: str) -> RateLimitConfig:
    rate_limit_collection = mongodb.get_collection("rate_limits")

    user_limit = rate_limit_collection.find_one({"user_id": user_id})
    if not user_limit:
        logger.warning(f"Rate limit not found for user '{user_id}'")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Rate limit configuration not found"
        )

    logger.info(f"Fetched rate limit for user '{user_id}' successfully")
    return RateLimitConfig(user_id=user_limit["user_id"], limit=user_limit["limit"])

def set_rate_limit_handler(user_id: str, limit: int) -> dict:
    rate_limit_collection = mongodb.get_collection("rate_limits")

    existing = rate_limit_collection.find_one({"user_id": user_id})
    if existing:
        logger.warning(f"Attempted to set rate limit for existing user '{user_id}'")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Rate limit already set for user"
        )

    rate_limit_collection.insert_one({"user_id": user_id, "limit": limit})

    logger.info(f"Set new rate limit for user '{user_id}' to {limit}")
    return {"message": "Rate limit set successfully"}

def update_rate_limit_handler(user_id: str, limit: int) -> dict:
    rate_limit_collection = mongodb.get_collection("rate_limits")

    update_result = rate_limit_collection.update_one(
        {"user_id": user_id},
        {"$set": {"limit": limit}}
    )

    if update_result.matched_count == 0:
        logger.warning(f"Attempted to update non-existent rate limit for user '{user_id}'")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Rate limit configuration not found"
        )

    logger.info(f"Updated rate limit for user '{user_id}' to {limit}")
    return {"message": "Rate limit updated successfully"}
