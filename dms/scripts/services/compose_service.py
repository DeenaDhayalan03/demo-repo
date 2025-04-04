from fastapi import APIRouter, HTTPException
from scripts.models.compose_model import ComposeUpRequest, ComposeDownRequest, ComposeLogsRequest, ComposeStatusRequest
from scripts.handlers.compose_handler import compose_up_service, compose_down_service, retrieve_compose_logs_service, retrieve_compose_status_service
from scripts.constants.app_constants import (
    COMPOSE_UP_FAILURE,
    COMPOSE_DOWN_FAILURE,
)
from scripts.constants.api_endpoints import (
    COMPOSE_UP, COMPOSE_DOWN, COMPOSE_LOGS, COMPOSE_STATUS
)
from scripts.logging import logger

router = APIRouter()

@router.post(COMPOSE_UP)
async def compose_up(compose_request: ComposeUpRequest):
    logger.info(f"Received Docker Compose UP request for project: {compose_request.project_name}")
    try:
        response = compose_up_service(compose_request)
        return response
    except Exception as e:
        logger.error(f"Compose UP failed for project {compose_request.project_name}: {str(e)}")
        raise HTTPException(status_code=COMPOSE_UP_FAILURE["status"], detail=str(e))

@router.post(COMPOSE_DOWN)
async def compose_down(compose_request: ComposeDownRequest):
    logger.info(f"Received Docker Compose DOWN request for project: {compose_request.project_name}")
    try:
        response = compose_down_service(compose_request)
        return response
    except Exception as e:
        logger.error(f"Compose DOWN failed for project {compose_request.project_name}: {str(e)}")
        raise HTTPException(status_code=COMPOSE_DOWN_FAILURE["status"], detail=str(e))

@router.post(COMPOSE_LOGS)
async def retrieve_logs(compose_request: ComposeLogsRequest):
    logger.info(f"Received request for logs of Compose project: {compose_request.project_name}")
    try:
        response = retrieve_compose_logs_service(compose_request)
        return response
    except Exception as e:
        logger.error(f"Failed to retrieve logs for Compose project {compose_request.project_name}: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@router.post(COMPOSE_STATUS)
async def retrieve_status(compose_request: ComposeStatusRequest):
    logger.info(f"Received request for status of Compose project: {compose_request.project_name}")
    try:
        response = retrieve_compose_status_service(compose_request)
        return response
    except Exception as e:
        logger.error(f"Failed to retrieve status for Compose project {compose_request.project_name}: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
