from fastapi import APIRouter
from scripts.handlers.image_handler import ImageHandler
from scripts.models.image_model import (
    ImageBuildRequest, ImagePushRequest, ImagePullRequest, ImageIDRequest
)
from scripts.constants.api_endpoints import (
    IMAGE_BUILD, IMAGE_PUSH, IMAGE_PULL, IMAGE_LIST, IMAGE_DETAILS, IMAGE_DELETE
)
from scripts.logging.logger import logger

router = APIRouter()
image_handler = ImageHandler()

@router.post(IMAGE_BUILD)
def build_image(request: ImageBuildRequest):
    logger.info("Received request to build Docker image.")
    return image_handler.build_image(request)

@router.post(IMAGE_PUSH)
def push_image(request: ImagePushRequest):
    logger.info(f"Received request to push Docker image: {request.repository}.")
    return image_handler.push_image(request)

@router.post(IMAGE_PULL)
def pull_image(request: ImagePullRequest):
    logger.info(f"Received request to pull Docker image: {request.repository}.")
    return image_handler.pull_image(request)

@router.get(IMAGE_LIST)
def list_images():
    logger.info("Received request to list all Docker images.")
    return image_handler.list_images()

@router.get(IMAGE_DETAILS)
def get_image_by_id(image_id: str):
    logger.info(f"Received request to get details for image ID: {image_id}.")
    return image_handler.get_image_by_id(image_id)

@router.delete(IMAGE_DELETE)
def delete_image(request: ImageIDRequest):
    logger.info(f"Received request to delete Docker image ID: {request.image_id}.")
    return image_handler.delete_image(request)
