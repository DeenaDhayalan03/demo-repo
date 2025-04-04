from pydantic import BaseModel, Field
from typing import Optional, List


class ImageBuildRequest(BaseModel):
    dockerfile_path: str = Field(..., title="Dockerfile Path", description="Path to the Dockerfile used for building the image.")
    tag: str = Field(..., title="Image Tag", description="Tag for the image being built.")
    context_path: Optional[str] = Field(".", title="Build Context Path", description="Context path for the Docker build. Defaults to current directory.")

class ImageBuildResponse(BaseModel):
    message: str = Field(..., title="Image Build Success Message", description="Success message confirming the image build.")
    image_id: str = Field(..., title="Built Image ID", description="Unique identifier of the built image.")


class ImagePushRequest(BaseModel):
    username: str = Field(..., title="Username", description="Username for Docker registry authentication.")
    password: str = Field(..., title="Password", description="Password for Docker registry authentication.")
    image_name: str = Field(..., title="Image Name (including tag)", description="Name of the image to push, including the tag.")
    registry_url: str = Field(..., title="Docker Registry URL", description="URL of the Docker registry for authentication.")
    repository: str = Field(..., title="Repository Name", description="Name of the repository to push the image to.")

class ImagePushResponse(BaseModel):
    message: str = Field(..., title="Image Push Success Message", description="Success message confirming the image push.")
    repository: str = Field(..., title="Repository Name", description="Name of the repository where the image was pushed.")


class ImagePullRequest(BaseModel):
    username: str = Field(..., title="Username", description="Username for Docker registry authentication.")
    password: str = Field(..., title="Password", description="Password for Docker registry authentication.")
    image_name: str = Field(..., title="Image Name (including tag)", description="Name of the image to pull, including the tag.")
    registry_url: str = Field(..., title="Docker Registry URL", description="URL of the Docker registry for authentication.")
    repository: str = Field(..., title="Repository Name", description="Name of the repository to pull the image from.")

class ImagePullResponse(BaseModel):
    message: str = Field(..., title="Image Pull Success Message", description="Success message confirming the image pull.")
    repository: str = Field(..., title="Repository Name", description="Name of the repository from where the image was pulled.")


class ImageDetailsResponse(BaseModel):
    image_id: str = Field(..., title="Image ID", description="Unique identifier of the Docker image.")
    repo_tags: List[str] = Field(..., title="Repository Tags", description="List of tags associated with the image.")
    size: int = Field(..., title="Image Size (in bytes)", description="Size of the image in bytes.")
    created: str = Field(..., title="Creation Timestamp", description="Timestamp of when the image was created.")

class ImageListResponse(BaseModel):
    images: List[ImageDetailsResponse] = Field(..., title="List of Docker Images", description="List containing details of available Docker images.")


class ImageIDRequest(BaseModel):
    image_id: str = Field(..., title="Image ID", description="Unique identifier of the image to be deleted.")

class ImageDeleteResponse(BaseModel):
    message: str = Field(..., title="Image Delete Success Message", description="Success message confirming the image deletion.")
    image_id: str = Field(..., title="Deleted Image ID", description="Unique identifier of the deleted image.")
