from fastapi import APIRouter
from scripts.handlers.compose_handler import ComposeHandler
from scripts.models.compose_model import (
    ComposeUpRequest,
    ComposeDownRequest,
    ComposeActionResponse
)
from scripts.constants.api_endpoints import (
    COMPOSE_UP,
    COMPOSE_DOWN
)
from scripts.logging.logger import logger

router = APIRouter()
compose_handler = ComposeHandler()

@router.post(COMPOSE_UP, response_model=ComposeActionResponse)
def compose_up(request: ComposeUpRequest):
    logger.info(f"Received request to start Compose services for project: {request.project_name}")
    return compose_handler.compose_up(request)

@router.post(COMPOSE_DOWN, response_model=ComposeActionResponse)
def compose_down(request: ComposeDownRequest):
    logger.info(f"Received request to stop Compose services for project: {request.project_name}")
    return compose_handler.compose_down(request)
