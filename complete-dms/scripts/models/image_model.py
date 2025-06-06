from pydantic import BaseModel
from typing import Optional, Union, IO, Any, Dict, List,Tuple,Literal
from io import StringIO


class ImageBuildRequest(BaseModel):
    path: Optional[str] = None
    fileobj: Optional[Union[StringIO, IO[bytes]]] = None
    tag: Optional[str] = None
    quiet: Optional[bool] = False
    nocache: Optional[bool] = False
    rm: Optional[bool] = False
    timeout: Optional[int] = None
    custom_context: Optional[bool] = False
    encoding: Optional[str] = None
    pull: Optional[bool] = False
    forcerm: Optional[bool] = False
    dockerfile: Optional[str] = None
    buildargs: Optional[Dict[str, Any]] = None
    container_limits: Optional[Dict[str, Any]] = None  # Simplified for now
    shmsize: Optional[int] = None
    labels: Optional[Dict[str, Any]] = None
    cache_from: Optional[List[str]] = None
    target: Optional[str] = None
    network_mode: Optional[str] = None
    squash: Optional[bool] = None
    extra_hosts: Optional[Union[List[str], Dict[str, str]]] = None
    platform: Optional[str] = None
    isolation: Optional[str] = None
    use_config_proxy: Optional[bool] = True

class ImageListRequest(BaseModel):
    name: Optional[str] = None
    all: Optional[bool] = False
    filters: Optional[Dict[str, Any]] = None

class ImageRemoveRequest(BaseModel):
    force: Optional[bool] = False
    noprune: Optional[bool] = False


class DockerLoginRequest(BaseModel):
    username: str
    password: str

class ImagePushRequest(BaseModel):
    local_tag: str
    remote_repo: str

class ImagePullRequest(BaseModel):
    repository: str
    local_tag: str = None