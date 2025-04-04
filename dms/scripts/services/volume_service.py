from fastapi import APIRouter
from scripts.models.volume_model import VolumeCreateRequest, VolumeCreateResponse, VolumeDetailsResponse, VolumeListResponse, VolumeActionResponse
from scripts.handlers.volume_handler import VolumeHandler
from scripts.constants.api_endpoints import VOLUME_CREATE, VOLUME_LIST, VOLUME_DETAILS, VOLUME_DELETE
from scripts.logging import logger
volume_handler = VolumeHandler()
router = APIRouter()

@router.post(VOLUME_CREATE, response_model=VolumeCreateResponse)
async def create_volume(request: VolumeCreateRequest):
    logger.info(f"Received request to create volume: {request.name}")
    return volume_handler.create_volume(request)

@router.get(VOLUME_LIST, response_model=VolumeListResponse)
async def list_volumes():
    logger.info("Received request to list all volumes.")
    return volume_handler.list_volumes()

@router.get(VOLUME_DETAILS, response_model=VolumeDetailsResponse)
async def get_volume_details(volume_id: str):
    logger.info(f"Received request to get details of volume ID: {volume_id}")
    return volume_handler.get_volume_details(volume_id)

@router.delete(VOLUME_DELETE, response_model=VolumeActionResponse)
async def remove_volume(volume_id: str):
    logger.info(f"Received request to delete volume ID: {volume_id}")
    return volume_handler.remove_volume(volume_id)
