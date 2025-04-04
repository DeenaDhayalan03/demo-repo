from scripts.utils.compose_utils import compose_up, compose_down, retrieve_compose_logs, retrieve_compose_status
from scripts.models.compose_model import ComposeUpRequest, ComposeDownRequest, ComposeLogsRequest, ComposeStatusRequest
from scripts.constants.app_constants import (
    COMPOSE_UP_SUCCESS, COMPOSE_UP_FAILURE,
    COMPOSE_DOWN_SUCCESS, COMPOSE_DOWN_FAILURE,
    COMPOSE_LOGS_RETRIEVED, COMPOSE_STATUS_RETRIEVED
)

def compose_up_service(compose_request: ComposeUpRequest) -> dict:
    try:
        result = compose_up(compose_request)
        return {
            "message": COMPOSE_UP_SUCCESS["message"],
            "status": COMPOSE_UP_SUCCESS["status"],
            "output": result["output"]
        }
    except Exception as e:
        raise Exception(COMPOSE_UP_FAILURE["message"] + ": " + str(e))

def compose_down_service(compose_request: ComposeDownRequest) -> dict:
    try:
        result = compose_down(compose_request)
        return {
            "message": COMPOSE_DOWN_SUCCESS["message"],
            "status": COMPOSE_DOWN_SUCCESS["status"],
            "output": result["output"]
        }
    except Exception as e:
        raise Exception(COMPOSE_DOWN_FAILURE["message"] + ": " + str(e))

def retrieve_compose_logs_service(compose_request: ComposeLogsRequest) -> dict:
    try:
        result = retrieve_compose_logs(compose_request)
        return {
            "message": COMPOSE_LOGS_RETRIEVED["message"],
            "status": COMPOSE_LOGS_RETRIEVED["status"],
            "output": result["output"]
        }
    except Exception as e:
        raise Exception("Failed to retrieve logs: " + str(e))

def retrieve_compose_status_service(compose_request: ComposeStatusRequest) -> dict:
    try:
        result = retrieve_compose_status(compose_request)
        return {
            "message": COMPOSE_STATUS_RETRIEVED["message"],
            "status": COMPOSE_STATUS_RETRIEVED["status"],
            "services": result["services"]
        }
    except Exception as e:
        raise Exception("Failed to retrieve status: " + str(e))
