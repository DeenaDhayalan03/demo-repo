from fastapi import APIRouter, Query, Body, Depends, HTTPException
from scripts.handlers.cont_handler import *
from scripts.models.cont_model import *
from scripts.constants.api_endpoints import Endpoints
from scripts.logging.logger import logger
from scripts.utils.jwt_utils import decode_access_token
from fastapi.security import OAuth2PasswordBearer

from typing import Optional

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login/")

def get_current_user(token: str = Depends(oauth2_scheme)):
    username = decode_access_token(token)
    if not username:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return username

container_router = APIRouter()

@container_router.post(Endpoints.CONTAINER_RUN)
def run_container_view(
    request: ContainerRunAdvancedRequest,
    username: str = Depends(get_current_user)
):
    logger.info(f"User '{username}' running container with basic parameters")
    return run_container_advanced(request, username=username)


@container_router.post(Endpoints.CONTAINER_RUN_ADV)
def run_container_advanced_view(
    data: ContainerRunAdvancedRequest,
    username: str = Depends(get_current_user)
):
    logger.info(f"User '{username}' running container with advanced parameters")
    return run_container_advanced(data, username=username)


@container_router.post(Endpoints.CONTAINER_LIST)
def list_containers_view(
    params: ContainerListRequest = Body(...),
    username: str = Depends(get_current_user)
):
    logger.info(f"User '{username}' listing containers with filters: {params.dict(exclude_unset=True)}")
    return list_containers_with_filters(params, username=username)


@container_router.post(Endpoints.CONTAINER_LOGS)
def get_container_logs(
    name: str,
    params: ContainerLogsRequest = Body(...),
    username: str = Depends(get_current_user)
):
    logger.info(f"User '{username}' fetching logs for container '{name}' with params: {params.dict(exclude_unset=True)}")
    return get_logs_with_params(name, params, username=username)


@container_router.post(Endpoints.CONTAINER_STOP)
def stop_container_view(
    name: str,
    timeout: Optional[float] = Query(None, description="Timeout in seconds before force stop"),
    username: str = Depends(get_current_user)
):
    logger.info(f"User '{username}' stopping container '{name}' with timeout={timeout}")
    return stop_container(name, timeout, username=username)


@container_router.post(Endpoints.CONTAINER_START)
def start_container_view(
    name: str,
    username: str = Depends(get_current_user)
):
    logger.info(f"User '{username}' starting container '{name}'")
    return start_container(name, username=username)


@container_router.post(Endpoints.CONTAINER_REMOVE)
def remove_container_view(
    name: str,
    params: ContainerRemoveRequest = Body(...),
    username: str = Depends(get_current_user)
):
    logger.info(f"User '{username}' removing container '{name}' with params: {params.dict(exclude_unset=True)}")
    return remove_container_with_params(name, params, username=username)
