from pydantic import BaseModel, Field
from typing import Optional, List

class ContainerWithVolumeRequest(BaseModel):
    image: str = Field(..., title="Docker Image", description="Name of the Docker image to use")
    name: Optional[str] = Field(None, title="Container Name", description="Custom name for the container")
    ports: Optional[List[str]] = Field(None, title="Port Mapping", description="List of ports like ['8080:80']")
    detach: bool = Field(default=True, title="Run in Background", description="Run the container in detached mode")
    volume_name: Optional[str] = Field(None, title="Volume Name", description="Name of the volume (optional)")
    mountpoint: str = Field(..., title="Mount Point", description="Path inside the container to mount volume")
    driver: Optional[str] = Field("local", title="Volume Driver", description="Docker volume driver (default: local)")


class ContainerWithVolumeResponse(BaseModel):
    message: str = Field(..., title="Message", description="Success message")
    container_id: str = Field(..., title="Container ID", description="ID of the created container")
    volume_name: str = Field(..., title="Volume Name", description="Name of the volume used")
    mountpoint: str = Field(..., title="Mount Point", description="Mount point inside the container")



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


class ContainerLogsResponse(BaseModel):
    container_id: str = Field(..., title="Container ID", description="ID of the container")
    logs: str = Field(..., title="Logs", description="Container logs output")


class ContainerActionResponse(BaseModel):
    message: str = Field(..., title="Message", description="Action success message")
    container_id: str = Field(..., title="Container ID", description="ID of the affected container")
