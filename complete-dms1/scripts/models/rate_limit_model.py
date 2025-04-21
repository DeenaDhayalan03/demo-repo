from pydantic import BaseModel

class RateLimitConfig(BaseModel):
    user_id: str
    limit: int
