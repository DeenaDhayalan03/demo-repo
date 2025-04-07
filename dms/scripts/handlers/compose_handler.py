from fastapi import HTTPException
from scripts.utils.compose_utils import ComposeUtils
from scripts.models.compose_model import (
    ComposeUpRequest, ComposeDownRequest, ComposeActionResponse
)
from scripts.logging.logger import logger
from scripts.constants.app_constants import (
    COMPOSE_UP_SUCCESS,
    COMPOSE_DOWN_SUCCESS
)


class ComposeHandler:
    def __init__(self):
        self.compose_utils = ComposeUtils()

    def compose_up(self, request: ComposeUpRequest) -> ComposeActionResponse:
        try:
            result = self.compose_utils.compose_up(request)
            logger.info("Docker Compose services started.")
            return ComposeActionResponse(message=COMPOSE_UP_SUCCESS, output=result)
        except HTTPException as e:
            logger.error(f"Docker Compose up failed: {e.detail}")
            raise e
        except Exception as e:
            logger.error(f"Unexpected error during compose up: {str(e)}")
            raise HTTPException(status_code=500, detail=str(e))

    def compose_down(self, request: ComposeDownRequest) -> ComposeActionResponse:
        try:
            result = self.compose_utils.compose_down(request)
            logger.info("Docker Compose services stopped.")
            return ComposeActionResponse(message=COMPOSE_DOWN_SUCCESS, output=result)
        except HTTPException as e:
            logger.error(f"Docker Compose down failed: {e.detail}")
            raise e
        except Exception as e:
            logger.error(f"Unexpected error during compose down: {str(e)}")
            raise HTTPException(status_code=500, detail=str(e))
