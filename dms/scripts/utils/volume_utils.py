import docker
from fastapi import HTTPException
from scripts.models.volume_model import VolumeCreateRequest, VolumeCreateResponse, VolumeDetailsResponse, VolumeListResponse, VolumeActionResponse
from scripts.constants.app_constants import (
    VOLUME_CREATE_SUCCESS, VOLUME_CREATE_FAILURE, VOLUME_REMOVE_SUCCESS,
    VOLUME_REMOVE_FAILURE, VOLUME_NOT_FOUND, VOLUME_RETRIEVE_FAILURE
)
from scripts.constants.app_configuration import settings

class VolumeUtils:
    def __init__(self):
        self.client = docker.DockerClient(base_url=settings.DOCKER_SOCK, timeout=settings.DOCKER_CLIENT_TIMEOUT)

    def create_volume(self, request: VolumeCreateRequest) -> VolumeCreateResponse:

        try:
            volume = self.client.volumes.create(name=request.name, driver=request.driver)
            return VolumeCreateResponse(
                message=VOLUME_CREATE_SUCCESS["message"],
                volume_name=volume.name,
                mountpoint=request.mountpoint
            )
        except Exception:
            raise HTTPException(status_code=VOLUME_CREATE_FAILURE["status"], detail=VOLUME_CREATE_FAILURE["message"])

    def list_volumes(self) -> VolumeListResponse:

        try:
            volumes = self.client.volumes.list()
            volume_names = [vol.name for vol in volumes]
            return VolumeListResponse(volumes=volume_names)
        except Exception:
            raise HTTPException(status_code=VOLUME_RETRIEVE_FAILURE["status"], detail=VOLUME_RETRIEVE_FAILURE["message"])

    def get_volume_details(self, volume_id: str) -> VolumeDetailsResponse:

        try:
            volume = self.client.volumes.get(volume_id)
            return VolumeDetailsResponse(
                name=volume.name,
                driver=volume.attrs.get("Driver"),
                mountpoint=volume.attrs.get("Mountpoint"),
                created_at=volume.attrs.get("CreatedAt")
            )
        except docker.errors.NotFound:
            raise HTTPException(status_code=VOLUME_NOT_FOUND["status"], detail=VOLUME_NOT_FOUND["message"])
        except Exception:
            raise HTTPException(status_code=VOLUME_RETRIEVE_FAILURE["status"], detail=VOLUME_RETRIEVE_FAILURE["message"])

    def remove_volume(self, volume_id: str) -> VolumeActionResponse:

        try:
            volume = self.client.volumes.get(volume_id)
            volume.remove()
            return VolumeActionResponse(
                message=VOLUME_REMOVE_SUCCESS["message"],
                volume_name=volume_id
            )
        except docker.errors.NotFound:
            raise HTTPException(status_code=VOLUME_NOT_FOUND["status"], detail=VOLUME_NOT_FOUND["message"])
        except Exception:
            raise HTTPException(status_code=VOLUME_REMOVE_FAILURE["status"], detail=VOLUME_REMOVE_FAILURE["message"])
