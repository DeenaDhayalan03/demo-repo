from scripts.utils.volume_utils import VolumeUtils
from scripts.models.volume_model import VolumeCreateRequest, VolumeCreateResponse, VolumeDetailsResponse, VolumeListResponse, VolumeActionResponse
from fastapi import HTTPException
from scripts.constants.app_constants import (
    VOLUME_CREATE_FAILURE,
    VOLUME_REMOVE_FAILURE,
    VOLUME_LIST_RETRIEVED, VOLUME_NOT_FOUND
)

class VolumeHandler:
    def __init__(self):
        self.volume_utils = VolumeUtils()

    def create_volume(self, request: VolumeCreateRequest) -> VolumeCreateResponse:
        try:
            result = self.volume_utils.create_volume(request)
            return VolumeCreateResponse(
                message=result.message,
                volume_name=result.volume_name,
                mountpoint=request.mountpoint
            )
        except Exception:
            raise HTTPException(status_code=VOLUME_CREATE_FAILURE["status"], detail=VOLUME_CREATE_FAILURE["message"])

    def list_volumes(self) -> VolumeListResponse:
        try:
            volumes = self.volume_utils.list_volumes()
            return VolumeListResponse(volumes=volumes.volumes)
        except Exception:
            raise HTTPException(status_code=VOLUME_LIST_RETRIEVED["status"], detail=VOLUME_LIST_RETRIEVED["message"])

    def get_volume_details(self, volume_id: str) -> VolumeDetailsResponse:
        try:
            volume_details = self.volume_utils.get_volume_details(volume_id)
            return VolumeDetailsResponse(
                name=volume_details.name,
                driver=volume_details.driver,
                mountpoint=volume_details.mountpoint,
                created_at=volume_details.created_at
            )
        except Exception:
            raise HTTPException(status_code=VOLUME_NOT_FOUND["status"], detail=VOLUME_NOT_FOUND["message"])

    def remove_volume(self, volume_id: str) -> VolumeActionResponse:
        try:
            result = self.volume_utils.remove_volume(volume_id)
            return VolumeActionResponse(
                message=result.message,
                volume_name=result.volume_name
            )
        except Exception:
            raise HTTPException(status_code=VOLUME_REMOVE_FAILURE["status"], detail=VOLUME_REMOVE_FAILURE["message"])
