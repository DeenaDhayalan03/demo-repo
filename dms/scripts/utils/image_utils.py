import docker
from fastapi import HTTPException
from scripts.models.image_model import (
    ImageBuildRequest, ImagePushRequest, ImagePullRequest, ImageIDRequest,
    ImageBuildResponse, ImagePushResponse, ImagePullResponse, ImageDetailsResponse,
    ImageListResponse, ImageDeleteResponse
)
from scripts.constants.app_constants import (
    IMAGE_BUILD_FAILURE, IMAGE_PUSH_FAILURE, IMAGE_PULL_FAILURE, IMAGE_NOT_FOUND,
    IMAGE_REMOVE_FAILURE, NOT_FOUND_ERROR, INTERNAL_SERVER_ERROR
)
from scripts.constants.app_configuration import settings

class ImageUtils:
    def __init__(self):
        self.client = docker.DockerClient(base_url=settings.DOCKER_SOCK, timeout=settings.DOCKER_CLIENT_TIMEOUT)

    def build_image(self, request: ImageBuildRequest) -> ImageBuildResponse:
        try:
            image, _ = self.client.images.build(
                path=request.context_path,
                dockerfile=request.dockerfile_path,
                tag=request.tag
            )
            return ImageBuildResponse(message="Docker image built successfully.", image_id=image.id)
        except Exception as e:
            raise HTTPException(
                status_code=INTERNAL_SERVER_ERROR,
                detail=f"{IMAGE_BUILD_FAILURE['message']}: {str(e)}"
            )

    def push_image(self, request: ImagePushRequest) -> ImagePushResponse:
        try:
            self.client.login(username=request.username, password=request.password, registry=request.registry_url)
            push_result = self.client.images.push(request.repository)
            if "errorDetail" in push_result:
                raise HTTPException(
                    status_code=INTERNAL_SERVER_ERROR,
                    detail=f"{IMAGE_PUSH_FAILURE['message']}: {push_result}"
                )
            return ImagePushResponse(message="Docker image pushed successfully.", repository=request.repository)
        except Exception as e:
            raise HTTPException(
                status_code=INTERNAL_SERVER_ERROR,
                detail=f"{IMAGE_PUSH_FAILURE['message']}: {str(e)}"
            )

    def pull_image(self, request: ImagePullRequest) -> ImagePullResponse:
        try:
            self.client.login(username=request.username, password=request.password, registry=request.registry_url)
            image = self.client.images.pull(repository=request.repository)
            return ImagePullResponse(message="Docker image pulled successfully.", repository=request.repository)
        except Exception as e:
            raise HTTPException(
                status_code=INTERNAL_SERVER_ERROR,
                detail=f"{IMAGE_PULL_FAILURE['message']}: {str(e)}"
            )

    def list_images(self) -> ImageListResponse:
        try:
            images = self.client.images.list()
            image_list = [
                ImageDetailsResponse(
                    image_id=image.id,
                    repo_tags=image.tags,
                    size=image.attrs["Size"],
                    created=image.attrs["Created"]
                )
                for image in images
            ]
            return ImageListResponse(images=image_list)
        except Exception as e:
            raise HTTPException(
                status_code=INTERNAL_SERVER_ERROR,
                detail=f"Failed to list Docker images: {str(e)}"
            )

    def get_image_by_id(self, image_id: str) -> ImageDetailsResponse:
        try:
            image = self.client.images.get(image_id)
            return ImageDetailsResponse(
                image_id=image.id,
                repo_tags=image.tags,
                size=image.attrs["Size"],
                created=image.attrs["Created"]
            )
        except docker.errors.ImageNotFound:
            raise HTTPException(
                status_code=NOT_FOUND_ERROR,
                detail=IMAGE_NOT_FOUND['message']
            )
        except Exception as e:
            raise HTTPException(
                status_code=INTERNAL_SERVER_ERROR,
                detail=f"Failed to retrieve image details: {str(e)}"
            )

    def delete_image(self, request: ImageIDRequest) -> ImageDeleteResponse:
        try:
            self.client.images.remove(image=request.image_id)
            return ImageDeleteResponse(message="Docker image deleted successfully.", image_id=request.image_id)
        except docker.errors.ImageNotFound:
            raise HTTPException(
                status_code=NOT_FOUND_ERROR,
                detail=IMAGE_NOT_FOUND['message']
            )
        except Exception as e:
            raise HTTPException(
                status_code=INTERNAL_SERVER_ERROR,
                detail=f"{IMAGE_REMOVE_FAILURE['message']}: {str(e)}"
            )
