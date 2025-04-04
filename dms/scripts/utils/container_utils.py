import docker
from fastapi import HTTPException
from scripts.models.container_model import (
    ContainerCreateRequest, ContainerCreateResponse, ContainerLogsResponse, ContainerActionResponse
)
from scripts.constants.app_constants import (
    CONTAINER_CREATE_SUCCESS, CONTAINER_CREATE_FAILURE,
    CONTAINER_STOP_SUCCESS, CONTAINER_STOP_FAILURE,
    CONTAINER_RESTART_SUCCESS, CONTAINER_RESTART_FAILURE,
    CONTAINER_REMOVE_SUCCESS, CONTAINER_REMOVE_FAILURE,
    CONTAINER_LOGS_RETRIEVED, CONTAINER_LOGS_FAILURE,
    CONTAINER_LIST_RETRIEVED, CONTAINER_NOT_FOUND
)
from scripts.constants.app_configuration import settings

class ContainerUtils:
    def __init__(self):
        self.client = docker.DockerClient(base_url=settings.DOCKER_SOCK, timeout=settings.DOCKER_CLIENT_TIMEOUT)

    def create_container(self, request: ContainerCreateRequest) -> ContainerCreateResponse:
        try:
            ports = {p.split(":")[1]: p.split(":")[0] for p in request.ports} if request.ports else None
            container = self.client.containers.create(
                image=request.image,
                name=request.name if request.name else None,
                ports=ports if ports else None,
                detach=request.detach
            )
            return ContainerCreateResponse(
                message=CONTAINER_CREATE_SUCCESS["message"],
                container_id=container.id
            )
        except Exception as e:
            raise HTTPException(
                status_code=CONTAINER_CREATE_FAILURE["status"],
                detail=f"{CONTAINER_CREATE_FAILURE['message']}: {str(e)}"
            )

    def stop_container(self, container_id: str) -> ContainerActionResponse:
        try:
            container = self.client.containers.get(container_id)
            container.stop()
            return ContainerActionResponse(
                message=CONTAINER_STOP_SUCCESS["message"],
                container_id=container_id
            )
        except docker.errors.NotFound:
            raise HTTPException(status_code=CONTAINER_NOT_FOUND["status"], detail=CONTAINER_NOT_FOUND["message"])
        except Exception as e:
            raise HTTPException(
                status_code=CONTAINER_STOP_FAILURE["status"],
                detail=f"{CONTAINER_STOP_FAILURE['message']}: {str(e)}"
            )

    def restart_container(self, container_id: str) -> ContainerActionResponse:
        try:
            container = self.client.containers.get(container_id)
            container.restart()
            return ContainerActionResponse(
                message=CONTAINER_RESTART_SUCCESS["message"],
                container_id=container_id
            )
        except docker.errors.NotFound:
            raise HTTPException(status_code=CONTAINER_NOT_FOUND["status"], detail=CONTAINER_NOT_FOUND["message"])
        except Exception as e:
            raise HTTPException(
                status_code=CONTAINER_RESTART_FAILURE["status"],
                detail=f"{CONTAINER_RESTART_FAILURE['message']}: {str(e)}"
            )

    def get_container_logs(self, container_id: str) -> ContainerLogsResponse:
        try:
            container = self.client.containers.get(container_id)
            logs = container.logs().decode("utf-8").split("\n")
            return ContainerLogsResponse(
                container_id=container_id,
                logs=logs
            )
        except docker.errors.NotFound:
            raise HTTPException(status_code=CONTAINER_NOT_FOUND["status"], detail=CONTAINER_NOT_FOUND["message"])
        except Exception as e:
            raise HTTPException(
                status_code=CONTAINER_LOGS_FAILURE["status"],
                detail=f"{CONTAINER_LOGS_FAILURE['message']}: {str(e)}"
            )

    def list_containers(self):
        try:
            containers = self.client.containers.list(all=True)
            container_list = [
                {"container_id": container.id, "image": container.image.tags, "status": container.status}
                for container in containers
            ]
            return {
                "message": CONTAINER_LIST_RETRIEVED["message"],
                "containers": container_list
            }
        except Exception as e:
            raise HTTPException(
                status_code=CONTAINER_LOGS_FAILURE["status"],
                detail=f"{CONTAINER_LOGS_FAILURE['message']}: {str(e)}"
            )

    def get_container_details(self, container_id: str):
        try:
            container = self.client.containers.get(container_id)
            details = {
                "container_id": container.id,
                "image": container.image.tags,
                "status": container.status,
                "created": container.attrs["Created"],
                "network_settings": container.attrs["NetworkSettings"]
            }
            return {
                "message": CONTAINER_LOGS_RETRIEVED["message"],
                "container": details
            }
        except docker.errors.NotFound:
            raise HTTPException(status_code=CONTAINER_NOT_FOUND["status"], detail=CONTAINER_NOT_FOUND["message"])
        except Exception as e:
            raise HTTPException(
                status_code=CONTAINER_LOGS_FAILURE["status"],
                detail=f"Failed to retrieve container details: {str(e)}"
            )

    def remove_container(self, container_id: str) -> ContainerActionResponse:
        try:
            container = self.client.containers.get(container_id)
            container.remove(force=True)
            return ContainerActionResponse(
                message=CONTAINER_REMOVE_SUCCESS["message"],
                container_id=container_id
            )
        except docker.errors.NotFound:
            raise HTTPException(status_code=CONTAINER_NOT_FOUND["status"], detail=CONTAINER_NOT_FOUND["message"])
        except Exception as e:
            raise HTTPException(
                status_code=CONTAINER_REMOVE_FAILURE["status"],
                detail=f"{CONTAINER_REMOVE_FAILURE['message']}: {str(e)}"
            )
