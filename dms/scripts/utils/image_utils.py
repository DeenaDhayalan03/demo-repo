import docker
from fastapi import HTTPException
from scripts.models.image_model import (
    ImageBuildRequest, ImagePushRequest, ImagePullRequest, ImageIDRequest,
    ImageBuildResponse, ImagePushResponse, ImagePullResponse, ImageDetailsResponse,
    ImageListResponse, ImageDeleteResponse
)
from scripts.constants.app_constants import (
    IMAGE_BUILD_FAILURE, IMAGE_BUILD_SUCCESS,
    IMAGE_PUSH_FAILURE, IMAGE_PUSH_SUCCESS,
    IMAGE_PULL_FAILURE, IMAGE_PULL_SUCCESS,
    IMAGE_REMOVE_FAILURE, IMAGE_REMOVE_SUCCESS,
    IMAGE_NOT_FOUND, IMAGE_LIST_RETRIEVED,
    INTERNAL_SERVER_ERROR
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
            return ImageBuildResponse(message=IMAGE_BUILD_SUCCESS, image_id=image.id)
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"{IMAGE_BUILD_FAILURE}: {str(e)}"
            )

    def push_image(self, request: ImagePushRequest) -> ImagePushResponse:
        try:
            self.client.login(
                username=request.username,
                password=request.password,
                registry=request.registry_url
            )
            push_result = self.client.images.push(request.repository)
            if "errorDetail" in push_result:
                raise HTTPException(
                    status_code=500,
                    detail=f"{IMAGE_PUSH_FAILURE}: {push_result}"
                )
            return ImagePushResponse(message=IMAGE_PUSH_SUCCESS, repository=request.repository)
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"{IMAGE_PUSH_FAILURE}: {str(e)}"
            )

    def pull_image(self, request: ImagePullRequest) -> ImagePullResponse:
        try:
            image = self.client.images.pull(repository=request.image_name)
            return ImagePullResponse(message=IMAGE_PULL_SUCCESS, repository=request.image_name)
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"{IMAGE_PULL_FAILURE}: {str(e)}"
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
            return ImageListResponse(images=image_list, message=IMAGE_LIST_RETRIEVED)
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"{INTERNAL_SERVER_ERROR}: {str(e)}"
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
                status_code=404,
                detail=IMAGE_NOT_FOUND
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"{INTERNAL_SERVER_ERROR}: {str(e)}"
            )

    def delete_image(self, request: ImageIDRequest) -> ImageDeleteResponse:
        try:
            containers = self.client.containers.list(all=True, filters={"ancestor": request.image_id})
            for container in containers:
                try:
                    container.remove(force=True)
                except Exception as ce:
                    raise HTTPException(
                        status_code=500,
                        detail=f"Failed to remove container {container.id} using the image: {str(ce)}"
                    )
            self.client.images.remove(image=request.image_id, force=True)
            return ImageDeleteResponse(message=IMAGE_REMOVE_SUCCESS, image_id=request.image_id)
        except docker.errors.ImageNotFound:
            raise HTTPException(
                status_code=404,
                detail=IMAGE_NOT_FOUND
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"{IMAGE_REMOVE_FAILURE}: {str(e)}"
            )
