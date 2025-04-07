from fastapi import APIRouter
from scripts.handlers.cont_vol_handler import ContainerWithVolumeHandler
from scripts.models.cont_vol_model import (
    ContainerWithVolumeRequest, ContainerWithVolumeResponse,
    ContainerLogsResponse, ContainerActionResponse, VolumeDetailsResponse,
    VolumeListResponse, VolumeActionResponse
)
from scripts.constants.api_endpoints import (
    CONTAINER_CREATE, CONTAINER_STOP,
    CONTAINER_START, CONTAINER_LOGS,
    CONTAINER_LIST, CONTAINER_DETAILS, CONTAINER_DELETE,
    VOLUME_LIST, VOLUME_DETAILS, VOLUME_DELETE
)
from scripts.logging.logger import logger

router = APIRouter()
container_vol_handler = ContainerWithVolumeHandler()

@router.post(CONTAINER_CREATE, response_model=ContainerWithVolumeResponse)
def create_container(request: ContainerWithVolumeRequest):
    logger.info(f"Received request to create container with image: {request.image}")
    return container_vol_handler.create_container_with_volume(request)

@router.post(CONTAINER_STOP, response_model=ContainerActionResponse)
def stop_container(container_id: str):
    logger.info(f"Received request to stop container ID: {container_id}")
    return container_vol_handler.stop_container(container_id)

@router.post(CONTAINER_START, response_model=ContainerActionResponse)
def start_container(container_id: str):
    logger.info(f"Received request to start container ID: {container_id}")
    return container_vol_handler.start_container(container_id)

@router.get(CONTAINER_LOGS, response_model=ContainerLogsResponse)
def get_container_logs(container_id: str):
    logger.info(f"Received request to fetch logs of container ID: {container_id}")
    return container_vol_handler.get_container_logs(container_id)

@router.get(CONTAINER_LIST)
def list_containers():
    logger.info("Received request to list all containers.")
    return container_vol_handler.list_containers()

@router.get(CONTAINER_DETAILS)
def get_container_details(container_id: str):
    logger.info(f"Received request to get details for container ID: {container_id}")
    return container_vol_handler.get_container_details(container_id)

@router.delete(CONTAINER_DELETE, response_model=ContainerActionResponse)
def remove_container(container_id: str):
    logger.info(f"Received request to delete container ID: {container_id}")
    return container_vol_handler.remove_container(container_id)

@router.get(VOLUME_LIST, response_model=VolumeListResponse)
def list_volumes():
    logger.info("Received request to list all volumes.")
    return container_vol_handler.list_volumes()

@router.get(VOLUME_DETAILS, response_model=VolumeDetailsResponse)
def get_volume_details(volume_id: str):
    logger.info(f"Received request to get details of volume ID: {volume_id}")
    return container_vol_handler.get_volume_details(volume_id)

@router.delete(VOLUME_DELETE, response_model=VolumeActionResponse)
def remove_volume(volume_id: str):
    logger.info(f"Received request to delete volume ID: {volume_id}")
    return container_vol_handler.remove_volume(volume_id)
