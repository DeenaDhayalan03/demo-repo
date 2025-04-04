import docker
import subprocess
from fastapi import HTTPException
from scripts.constants.app_constants import (
    PRUNE_IMAGES_SUCCESS, PRUNE_CONTAINERS_SUCCESS, PRUNE_VOLUMES_SUCCESS, PRUNE_SYSTEM_SUCCESS,
    PRUNE_IMAGES_FAILURE, PRUNE_CONTAINERS_FAILURE, PRUNE_VOLUMES_FAILURE, PRUNE_SYSTEM_FAILURE
)
from scripts.models.prune_model import PruneResponse
from scripts.constants.app_configuration import settings

class PruneUtils:
    def __init__(self):
        self.client = docker.DockerClient(
            base_url=settings.DOCKER_SOCK,
            timeout=settings.DOCKER_CLIENT_TIMEOUT
        )


def run_prune_command(command: str) -> str:
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error occurred while running prune command: {e.stderr.decode('utf-8')}"
        )


def prune_images(force: bool) -> PruneResponse:
    command = "docker image prune -f" if force else "docker image prune"
    output = run_prune_command(command)

    if output:
        return PruneResponse(
            message=PRUNE_IMAGES_SUCCESS["message"],
            deleted_items=[output],
            reclaimed_space=0
        )

    raise HTTPException(
        status_code=PRUNE_IMAGES_FAILURE["status"],
        detail=PRUNE_IMAGES_FAILURE["message"]
    )


def prune_containers(force: bool) -> PruneResponse:
    command = "docker container prune -f" if force else "docker container prune"
    output = run_prune_command(command)

    if output:
        return PruneResponse(
            message=PRUNE_CONTAINERS_SUCCESS["message"],
            deleted_items=[output],
            reclaimed_space=0
        )

    raise HTTPException(
        status_code=PRUNE_CONTAINERS_FAILURE["status"],
        detail=PRUNE_CONTAINERS_FAILURE["message"]
    )


def prune_volumes(force: bool) -> PruneResponse:
    command = "docker volume prune -f" if force else "docker volume prune"
    output = run_prune_command(command)

    if output:
        return PruneResponse(
            message=PRUNE_VOLUMES_SUCCESS["message"],
            deleted_items=[output],
            reclaimed_space=0
        )

    raise HTTPException(
        status_code=PRUNE_VOLUMES_FAILURE["status"],
        detail=PRUNE_VOLUMES_FAILURE["message"]
    )


def prune_all(force: bool) -> PruneResponse:
    command = "docker system prune -af" if force else "docker system prune -a"
    output = run_prune_command(command)

    if output:
        return PruneResponse(
            message=PRUNE_SYSTEM_SUCCESS["message"],
            deleted_items=[output],
            reclaimed_space=0
        )

    raise HTTPException(
        status_code=PRUNE_SYSTEM_FAILURE["status"],
        detail=PRUNE_SYSTEM_FAILURE["message"]
    )