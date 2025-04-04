from fastapi import HTTPException
from scripts.models.prune_model import PruneRequest, PruneResponse
from scripts.utils.prune_utils import PruneUtils
from scripts.constants.app_constants import (
    PRUNE_IMAGES_FAILURE,
    PRUNE_CONTAINERS_FAILURE,
    PRUNE_VOLUMES_FAILURE,
    PRUNE_SYSTEM_FAILURE
)

class PruneHandler:
    def __init__(self):
        self.prune_utils = PruneUtils()

    def prune_images(self, request: PruneRequest) -> PruneResponse:
        try:
            return self.prune_utils.prune_images(request.force)
        except Exception:
            raise HTTPException(status_code=PRUNE_IMAGES_FAILURE["status"], detail=PRUNE_IMAGES_FAILURE["message"])

    def prune_containers(self, request: PruneRequest) -> PruneResponse:
        try:
            return self.prune_utils.prune_containers(request.force)
        except Exception:
            raise HTTPException(status_code=PRUNE_CONTAINERS_FAILURE["status"], detail=PRUNE_CONTAINERS_FAILURE["message"])

    def prune_volumes(self, request: PruneRequest) -> PruneResponse:
        try:
            return self.prune_utils.prune_volumes(request.force)
        except Exception:
            raise HTTPException(status_code=PRUNE_VOLUMES_FAILURE["status"], detail=PRUNE_VOLUMES_FAILURE["message"])

    def prune_all(self, request: PruneRequest) -> PruneResponse:
        try:
            return self.prune_utils.prune_all(request.force)
        except Exception:
            raise HTTPException(status_code=PRUNE_SYSTEM_FAILURE["status"], detail=PRUNE_SYSTEM_FAILURE["message"])
