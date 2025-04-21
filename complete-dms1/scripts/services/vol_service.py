from fastapi import APIRouter, Body, Path, Depends, status
from scripts.handlers.vol_handler import *
from scripts.models.volume_model import *
from scripts.constants.api_endpoints import Endpoints
from scripts.logging.logger import logger
from scripts.utils.jwt_utils import get_current_user_from_token

volume_router = APIRouter()

def get_current_user(token: str = Depends(get_current_user_from_token)):
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    return token

@volume_router.post(Endpoints.VOLUME_CREATE)
def create_volume_advanced(
    data: VolumeCreateRequest = Body(...),
    current_user: str = Depends(get_current_user)
):
    logger.info(f"User '{current_user}' is creating volume with params: {data.dict(exclude_unset=True)}")
    return create_volume_with_params(data, current_user)


@volume_router.delete(Endpoints.VOLUME_DELETE)
def delete_volume(
    name: str = Path(..., description="Name of the Docker volume"),
    params: VolumeRemoveRequest = Body(...),
    current_user: str = Depends(get_current_user)
):
    logger.info(f"User '{current_user}' is deleting volume '{name}' with options: {params.dict(exclude_unset=True)}")
    return remove_volume_with_params(name, params, current_user)
