from pydantic import BaseModel, Field
from typing import Optional, List

class ContainerCreateRequest(BaseModel):
    image: str = Field(..., title="Docker Image", description="Name of the Docker image to use")
    name: Optional[str] = Field(None, title="Container Name", description="Custom name for the container")
    ports: Optional[List[str]] = Field(None, title="Port Mapping", description="List of ports in 'host:container' format (e.g., '8080:80')")
    detach: bool = Field(default=True, title="Run in Background", description="Run the container in detached mode")

class ContainerCreateResponse(BaseModel):
    message: str = Field(..., title="Message", description="Success message")
    container_id: str = Field(..., title="Container ID", description="ID of the created container")

class ContainerLogsResponse(BaseModel):
    container_id: str = Field(..., title="Container ID", description="ID of the container")
    logs: List[str] = Field(..., title="Logs", description="Container logs output")

class ContainerActionResponse(BaseModel):
    message: str = Field(..., title="Message", description="Action success message")
    container_id: str = Field(..., title="Container ID", description="ID of the affected container")
