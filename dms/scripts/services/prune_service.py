from fastapi import APIRouter
from scripts.models.prune_model import PruneRequest, PruneResponse
from scripts.handlers.prune_handler import PruneHandler
from scripts.constants.api_endpoints import (
    PRUNE_IMAGES,
    PRUNE_CONTAINERS,
    PRUNE_VOLUMES,
    PRUNE_ALL
)
from scripts.logging import logger

router = APIRouter()
prune_handler = PruneHandler()

@router.post(PRUNE_IMAGES, response_model=PruneResponse)
async def prune_images(request: PruneRequest):
    logger.info("Received request to prune unused Docker images.")
    return prune_handler.prune_images(request)

@router.post(PRUNE_CONTAINERS, response_model=PruneResponse)
async def prune_containers(request: PruneRequest):
    logger.info("Received request to prune stopped Docker containers.")
    return prune_handler.prune_containers(request)

@router.post(PRUNE_VOLUMES, response_model=PruneResponse)
async def prune_volumes(request: PruneRequest):
    logger.info("Received request to prune unused Docker volumes.")
    return prune_handler.prune_volumes(request)

@router.post(PRUNE_ALL, response_model=PruneResponse)
async def prune_all(request: PruneRequest):
    logger.info("Received request to prune all unused Docker resources (images, containers, volumes).")
    return prune_handler.prune_all(request)
