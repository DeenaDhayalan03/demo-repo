from scripts.utils.image_utils import ImageUtils
from scripts.models.image_model import (
    ImageBuildRequest, ImageBuildResponse,
    ImagePushRequest, ImagePushResponse,
    ImagePullRequest, ImagePullResponse,
    ImageIDRequest, ImageDeleteResponse,
    ImageListResponse, ImageDetailsResponse
)
from fastapi import HTTPException
from scripts.logging.logger import logger


class ImageHandler:
    def __init__(self):
        self.image_utils = ImageUtils()

    def build_image(self, request: ImageBuildRequest) -> ImageBuildResponse:
        try:
            response = self.image_utils.build_image(request)
            logger.info(f"Image built successfully: {response.image_id}")
            return response
        except HTTPException as e:
            logger.error(f"Image build failed: {e.detail}")
            raise e

    def push_image(self, request: ImagePushRequest) -> ImagePushResponse:
        try:
            response = self.image_utils.push_image(request)
            logger.info(f"Image pushed to {response.repository}")
            return response
        except HTTPException as e:
            logger.error(f"Image push failed: {e.detail}")
            raise e

    def pull_image(self, request: ImagePullRequest) -> ImagePullResponse:
        try:
            response = self.image_utils.pull_image(request)
            logger.info(f"Image pulled from {response.repository}")
            return response
        except HTTPException as e:
            logger.error(f"Image pull failed: {e.detail}")
            raise e

    def list_images(self) -> ImageListResponse:
        try:
            response = self.image_utils.list_images()
            logger.info(f"{len(response.images)} images listed")
            return response
        except HTTPException as e:
            logger.error(f"List images failed: {e.detail}")
            raise e

    def get_image_by_id(self, image_id: str) -> ImageDetailsResponse:
        try:
            response = self.image_utils.get_image_by_id(image_id)
            logger.info(f"Retrieved image: {response.image_id}")
            return response
        except HTTPException as e:
            logger.error(f"Get image by ID failed: {e.detail}")
            raise e

    def delete_image(self, request: ImageIDRequest) -> ImageDeleteResponse:
        try:
            response = self.image_utils.delete_image(request)
            logger.info(f"Deleted image: {response.image_id}")
            return response
        except HTTPException as e:
            logger.error(f"Delete image failed: {e.detail}")
            raise e
