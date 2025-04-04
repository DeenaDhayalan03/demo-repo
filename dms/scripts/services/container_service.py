from fastapi import APIRouter
from scripts.handlers.container_handler import ContainerHandler
from scripts.models.container_model import (
    ContainerCreateRequest, ContainerCreateResponse,
    ContainerLogsResponse, ContainerActionResponse
)
from scripts.constants.api_endpoints import (
    CONTAINER_CREATE, CONTAINER_STOP, CONTAINER_RESTART,
    CONTAINER_LOGS, CONTAINER_LIST, CONTAINER_DETAILS, CONTAINER_DELETE
)
from scripts.logging import logger

router = APIRouter()
container_handler = ContainerHandler()

@router.post(CONTAINER_CREATE, response_model=ContainerCreateResponse)
def create_container(request: ContainerCreateRequest):
    logger.info(f"Received request to create container with image: {request.image}")
    return container_handler.create_container(request)

@router.post(CONTAINER_STOP, response_model=ContainerActionResponse)
def stop_container(container_id: str):
    logger.info(f"Received request to stop container ID: {container_id}")
    return container_handler.stop_container(container_id)

@router.post(CONTAINER_RESTART, response_model=ContainerActionResponse)
def restart_container(container_id: str):
    logger.info(f"Received request to restart container ID: {container_id}")
    return container_handler.restart_container(container_id)

@router.get(CONTAINER_LOGS, response_model=ContainerLogsResponse)
def get_container_logs(container_id: str):
    logger.info(f"Received request to fetch logs of container ID: {container_id}")
    return container_handler.get_container_logs(container_id)

@router.get(CONTAINER_LIST)
def list_containers():
    logger.info("Received request to list all containers.")
    return container_handler.list_containers()

@router.get(CONTAINER_DETAILS)
def get_container_details(container_id: str):
    logger.info(f"Received request to get details for container ID: {container_id}")
    return container_handler.get_container_details(container_id)

@router.delete(CONTAINER_DELETE, response_model=ContainerActionResponse)
def remove_container(container_id: str):
    logger.info(f"Received request to delete container ID: {container_id}")
    return container_handler.remove_container(container_id)
