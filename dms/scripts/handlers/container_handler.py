from fastapi import HTTPException
from scripts.utils.container_utils import ContainerUtils
from scripts.models.container_model import (
    ContainerCreateRequest, ContainerCreateResponse,
    ContainerLogsResponse, ContainerActionResponse
)
from scripts.constants.app_constants import (
    CONTAINER_CREATE_FAILURE, CONTAINER_STOP_FAILURE,
    CONTAINER_RESTART_FAILURE, CONTAINER_LOGS_FAILURE,
    CONTAINER_REMOVE_FAILURE
)

class ContainerHandler:
    def __init__(self):
        self.container_utils = ContainerUtils()

    def create_container(self, request: ContainerCreateRequest) -> ContainerCreateResponse:
        try:
            return self.container_utils.create_container(request)
        except Exception as e:
            raise HTTPException(
                status_code=CONTAINER_CREATE_FAILURE["status"],
                detail=f"{CONTAINER_CREATE_FAILURE['message']}: {str(e)}"
            )

    def stop_container(self, container_id: str) -> ContainerActionResponse:
        try:
            return self.container_utils.stop_container(container_id)
        except Exception as e:
            raise HTTPException(
                status_code=CONTAINER_STOP_FAILURE["status"],
                detail=f"{CONTAINER_STOP_FAILURE['message']}: {str(e)}"
            )

    def restart_container(self, container_id: str) -> ContainerActionResponse:
        try:
            return self.container_utils.restart_container(container_id)
        except Exception as e:
            raise HTTPException(
                status_code=CONTAINER_RESTART_FAILURE["status"],
                detail=f"{CONTAINER_RESTART_FAILURE['message']}: {str(e)}"
            )

    def get_container_logs(self, container_id: str) -> ContainerLogsResponse:
        try:
            return self.container_utils.get_container_logs(container_id)
        except Exception as e:
            raise HTTPException(
                status_code=CONTAINER_LOGS_FAILURE["status"],
                detail=f"{CONTAINER_LOGS_FAILURE['message']}: {str(e)}"
            )

    def list_containers(self):
        try:
            return self.container_utils.list_containers()
        except Exception as e:
            raise HTTPException(
                status_code=CONTAINER_LOGS_FAILURE["status"],
                detail=f"{CONTAINER_LOGS_FAILURE['message']}: {str(e)}"
            )

    def get_container_details(self, container_id: str):
        try:
            return self.container_utils.get_container_details(container_id)
        except Exception as e:
            raise HTTPException(
                status_code=CONTAINER_LOGS_FAILURE["status"],
                detail=f"{CONTAINER_LOGS_FAILURE['message']}: {str(e)}"
            )

    def remove_container(self, container_id: str) -> ContainerActionResponse:
        try:
            return self.container_utils.remove_container(container_id)
        except Exception as e:
            raise HTTPException(
                status_code=CONTAINER_REMOVE_FAILURE["status"],
                detail=f"{CONTAINER_REMOVE_FAILURE['message']}: {str(e)}"
            )
