from fastapi import HTTPException
from datetime import datetime, timedelta
from scripts.utils.mongo_utils import MongoDBConnection
from scripts.constants.app_configuration import settings

mongo = MongoDBConnection()

MAX_CONTAINERS_PER_HOUR = settings.max_containers_per_user

def check_rate_limit(user_id: str) -> bool:
    one_hour_ago = datetime.utcnow() - timedelta(hours=1)

    containers_collection = mongo.get_collection("user_containers")

    user_containers = containers_collection.find({
        "user_id": user_id,
        "created_time": {"$gte": one_hour_ago}
    })

    container_count = user_containers.count()

    if container_count >= MAX_CONTAINERS_PER_HOUR:
        raise HTTPException(
            status_code=429,
            detail=f"Rate limit exceeded. You can only create {MAX_CONTAINERS_PER_HOUR} containers per hour."
        )

    return True
