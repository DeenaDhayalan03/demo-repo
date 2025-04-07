import docker
from fastapi import HTTPException
from docker.errors import NotFound
from scripts.constants.app_configuration import settings
from scripts.constants import app_constants as constants
from scripts.models.cont_vol_model import (
    ContainerWithVolumeRequest, ContainerWithVolumeResponse,
    VolumeDetailsResponse, VolumeListResponse, VolumeActionResponse,
    ContainerActionResponse, ContainerLogsResponse
)


class ContainerWithVolumeUtils:
    def __init__(self):
        self.client = docker.DockerClient(base_url=settings.DOCKER_SOCK, timeout=settings.DOCKER_CLIENT_TIMEOUT)

    def create_container_with_volume(self, request: ContainerWithVolumeRequest) -> ContainerWithVolumeResponse:
        try:
            if request.volume_name:
                volume = self.client.volumes.create(name=request.volume_name, driver=request.driver)
            else:
                volume = self.client.volumes.create(driver=request.driver)

            ports = {p.split(":")[1]: p.split(":")[0] for p in request.ports} if request.ports else None

            container = self.client.containers.create(
                image=request.image,
                name=request.name if request.name else None,
                ports=ports,
                detach=request.detach,
                volumes={volume.name: {'bind': request.mountpoint, 'mode': 'rw'}}
            )

            return ContainerWithVolumeResponse(
                message=constants.CONTAINER_CREATE_SUCCESS,
                container_id=container.id,
                volume_name=volume.name,
                mountpoint=request.mountpoint
            )

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"{constants.CONTAINER_CREATE_FAILURE}: {str(e)}"
            )


    def stop_container(self, container_id: str) -> ContainerActionResponse:
        try:
            container = self.client.containers.get(container_id)
            container.stop()
            return ContainerActionResponse(
                message=constants.CONTAINER_STOP_SUCCESS,
                container_id=container_id
            )
        except NotFound:
            raise HTTPException(status_code=404, detail=constants.CONTAINER_NOT_FOUND)
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"{constants.CONTAINER_STOP_FAILURE}: {str(e)}"
            )


    def start_container(self, container_id: str) -> ContainerActionResponse:
        try:
            container = self.client.containers.get(container_id)
            container.start()
            return ContainerActionResponse(
                message=constants.CONTAINER_START_SUCCESS,
                container_id=container_id
            )
        except NotFound:
            raise HTTPException(status_code=404, detail=constants.CONTAINER_NOT_FOUND)
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"{constants.CONTAINER_START_FAILURE}: {str(e)}"
            )

    def get_container_logs(self, container_id: str) -> ContainerLogsResponse:
        try:
            container = self.client.containers.get(container_id)
            logs = container.logs(stdout=True, stderr=True, tail=100).decode("utf-8").split("\n")

            return ContainerLogsResponse(
                container_id=container_id,
                logs=logs
            )
        except NotFound:
            raise HTTPException(status_code=404, detail=constants.CONTAINER_NOT_FOUND)
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"{constants.CONTAINER_LOGS_FAILURE}: {str(e)}"
            )

    def list_containers(self):
        try:
            containers = self.client.containers.list(all=True)
            container_list = [
                {"container_id": container.id, "image": container.image.tags, "status": container.status}
                for container in containers
            ]
            return {
                "message": constants.CONTAINER_LIST_RETRIEVED,
                "containers": container_list
            }
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"{constants.INTERNAL_SERVER_ERROR}: {str(e)}"
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
                "message": constants.CONTAINER_LOGS_RETRIEVED,
                "container": details
            }
        except NotFound:
            raise HTTPException(status_code=404, detail=constants.CONTAINER_NOT_FOUND)
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"{constants.INTERNAL_SERVER_ERROR}: {str(e)}"
            )


    def remove_container(self, container_id: str) -> ContainerActionResponse:
        try:
            container = self.client.containers.get(container_id)
            container.remove(force=True)
            return ContainerActionResponse(
                message=constants.CONTAINER_REMOVE_SUCCESS,
                container_id=container_id
            )
        except NotFound:
            raise HTTPException(status_code=404, detail=constants.CONTAINER_NOT_FOUND)
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"{constants.CONTAINER_REMOVE_FAILURE}: {str(e)}"
            )


    def list_volumes(self) -> VolumeListResponse:
        try:
            volumes = self.client.volumes.list()
            volume_names = [vol.name for vol in volumes]
            return VolumeListResponse(volumes=volume_names)
        except Exception:
            raise HTTPException(status_code=500, detail=constants.VOLUME_RETRIEVE_FAILURE)


    def get_volume_details(self, volume_id: str) -> VolumeDetailsResponse:
        try:
            volume = self.client.volumes.get(volume_id)
            return VolumeDetailsResponse(
                name=volume.name,
                driver=volume.attrs.get("Driver"),
                mountpoint=volume.attrs.get("Mountpoint"),
                created_at=volume.attrs.get("CreatedAt")
            )
        except NotFound:
            raise HTTPException(status_code=404, detail=constants.VOLUME_NOT_FOUND)
        except Exception:
            raise HTTPException(status_code=500, detail=constants.VOLUME_RETRIEVE_FAILURE)


    def remove_volume(self, volume_id: str) -> VolumeActionResponse:
        try:
            volume = self.client.volumes.get(volume_id)
            volume.remove()
            return VolumeActionResponse(
                message=constants.VOLUME_REMOVE_SUCCESS,
                volume_name=volume_id
            )
        except NotFound:
            raise HTTPException(status_code=404, detail=constants.VOLUME_NOT_FOUND)
        except Exception:
            raise HTTPException(status_code=500, detail=constants.VOLUME_REMOVE_FAILURE)
