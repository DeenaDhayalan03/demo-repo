import docker
from fastapi import HTTPException
from scripts.models.volume_model import *
from scripts.constants.app_constants import (
    VOLUME_CREATE_SUCCESS,
    VOLUME_CREATE_FAILURE,
    VOLUME_REMOVE_SUCCESS,
    VOLUME_REMOVE_FAILURE,
    VOLUME_NOT_FOUND
)

client = docker.from_env()

def create_volume_with_params(data: VolumeCreateRequest):
    try:
        opts = data.dict(exclude_unset=True)
        volume = client.volumes.create(**opts)
        return {
            "message": f"{VOLUME_CREATE_SUCCESS}: '{volume.name}'",
            "name": volume.name,
            "driver": volume.attrs.get("Driver"),
            "labels": volume.attrs.get("Labels")
        }
    except Exception:
        raise HTTPException(status_code=500, detail=VOLUME_CREATE_FAILURE)


def remove_volume_with_params(name: str, params: VolumeRemoveRequest):
    try:
        opts = params.dict(exclude_unset=True)
        volume = client.volumes.get(name)
        volume.remove(**opts)
        return {"message": f"{VOLUME_REMOVE_SUCCESS}: '{name}'"}
    except docker.errors.NotFound:
        raise HTTPException(status_code=404, detail=VOLUME_NOT_FOUND)
    except Exception:
        raise HTTPException(status_code=500, detail=VOLUME_REMOVE_FAILURE)
