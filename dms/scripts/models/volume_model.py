from pydantic import BaseModel, Field
from typing import Optional, List

class VolumeCreateRequest(BaseModel):
    name: Optional[str] = Field(None, title="Volume Name", description="Custom name for the volume (optional)")
    driver: Optional[str] = Field("local", title="Volume Driver", description="Docker volume driver (default: local)")
    mountpoint: str = Field(..., title="Mount Path", description="Path inside the container where the volume should be mounted")

class VolumeCreateResponse(BaseModel):
    message: str = Field(..., title="Message", description="Volume creation success message")
    volume_name: str = Field(..., title="Volume Name", description="Name of the created volume")
    mountpoint: str = Field(..., title="Mount Path", description="Path where the volume is mounted inside the container")

class VolumeDetailsResponse(BaseModel):
    name: str = Field(..., title="Volume Name", description="Name of the volume")
    driver: str = Field(..., title="Driver", description="Docker volume driver used")
    mountpoint: str = Field(..., title="Mount Path", description="Path where the volume is mounted")
    created_at: str = Field(..., title="Created At", description="Timestamp when the volume was created")

class VolumeListResponse(BaseModel):
    volumes: List[str] = Field(..., title="Volumes", description="List of volume names")

class VolumeActionResponse(BaseModel):
    message: str = Field(..., title="Message", description="Action success message")
    volume_name: str = Field(..., title="Volume Name", description="Name of the affected volume")
