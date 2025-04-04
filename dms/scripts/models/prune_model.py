from pydantic import BaseModel, Field
from typing import List, Optional

class PruneRequest(BaseModel):
    resource_type: str = Field(..., title="Resource Type", description="Type of resource to prune (images, containers, volumes, all)")
    force: bool = False

class PruneResponse(BaseModel):
    message: str = Field(..., title="Prune Success Message")
    reclaimed_space: Optional[int] = Field(0, title="Reclaimed Space in Bytes")
    deleted_items: List[str] = Field([], title="List of Deleted Items")
