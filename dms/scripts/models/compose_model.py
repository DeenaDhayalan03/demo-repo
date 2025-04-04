from pydantic import BaseModel, Field
from typing import Optional, Dict, List

class ComposeUpRequest(BaseModel):
    compose_file_path: str = Field(..., title="Compose File Path", description="Path to the docker-compose.yml file")
    detach: bool = Field(default=True, title="Detached Mode", description="Run containers in the background (default is True)")

class ComposeDownRequest(BaseModel):
    compose_file_path: str = Field(..., title="Compose File Path", description="Path to the docker-compose.yml file")

class ComposeLogsRequest(BaseModel):
    compose_file_path: str = Field(..., title="Compose File Path", description="Path to the docker-compose.yml file")

class ComposeStatusRequest(BaseModel):
    compose_file_path: str = Field(..., title="Compose File Path", description="Path to the docker-compose.yml file")

class ComposeActionResponse(BaseModel):
    message: str = Field(..., title="Success Message")
    output: Optional[str] = Field(None, title="Output", description="Command output or details")

class ComposeStatusResponse(BaseModel):
    message: str = Field(..., title="Status Message")
    services: List[Dict[str, str]] = Field(..., title="Running Services Info", description="Information about the currently running containers")
