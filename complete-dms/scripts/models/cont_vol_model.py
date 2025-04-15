from pydantic import BaseModel
from typing import Optional, Union, Any, Dict, List,Tuple,Literal
from docker.types import Mount, Ulimit, EndpointConfig
from datetime import datetime

class ContainerRunAdvancedRequest(BaseModel):
    image: str
    command: Optional[Union[str, List[str]]] = None
    name: Optional[str] = None
    detach: Optional[bool] = True
    auto_remove: Optional[bool] = False
    stdout: Optional[bool] = True
    stderr: Optional[bool] = False
    remove: Optional[bool] = False
    mac_address: Optional[str] = None
    mem_limit: Optional[Union[str, int]] = None
    mem_reservation: Optional[Union[str, int]] = None
    mem_swappiness: Optional[int] = None
    memswap_limit: Optional[Union[str, int]] = None
    mounts: Optional[List[Mount]] = None
    nano_cpus: Optional[int] = None
    network: Optional[str] = None
    network_disabled: Optional[bool] = False
    network_mode: Optional[str] = None
    networking_config: Optional[Dict[str, EndpointConfig]] = None
    oom_kill_disable: Optional[bool] = False
    oom_score_adj: Optional[int] = None
    pid_mode: Optional[str] = None
    pids_limit: Optional[int] = None
    platform: Optional[str] = None
    ports: Optional[Dict[str, Union[int, List[int], Tuple[str, int], None]]] = None
    privileged: Optional[bool] = False
    publish_all_ports: Optional[bool] = False
    read_only: Optional[bool] = None
    restart_policy: Optional[Dict[str, Any]] = None  # or custom model if needed
    runtime: Optional[str] = None
    security_opt: Optional[List[str]] = None
    shm_size: Optional[Union[str, int]] = None
    stdin_open: Optional[bool] = False
    stop_signal: Optional[str] = None
    storage_opt: Optional[Dict[str, Any]] = None
    stream: Optional[bool] = False
    sysctls: Optional[Dict[str, Any]] = None
    tmpfs: Optional[Dict[str, str]] = None
    tty: Optional[bool] = False
    ulimits: Optional[List[Ulimit]] = None
    use_config_proxy: Optional[bool] = None
    user: Optional[Union[str, int]] = None
    userns_mode: Optional[str] = None
    uts_mode: Optional[str] = None
    version: Optional[str] = None
    volume_driver: Optional[str] = None
    volumes: Optional[Union[Dict[str, str], List[str]]] = None
    volumes_from: Optional[List[str]] = None
    working_dir: Optional[str] = None


class ContainerListRequest(BaseModel):
    all: Optional[bool] = False
    before: Optional[str] = None
    filters: Optional[Any] = None
    limit: Optional[int] = -1
    since: Optional[str] = None
    sparse: Optional[bool] = False
    ignore_removed: Optional[bool] = False


class ContainerLogsRequest(BaseModel):
    stdout: Optional[bool] = True
    stderr: Optional[bool] = True
    timestamps: Optional[bool] = False
    tail: Optional[Union[int, Literal["all"]]] = "all"
    since: Optional[Union[datetime, float]] = None
    until: Optional[Union[datetime, float]] = None
    follow: Optional[bool] = False


class ContainerRemoveRequest(BaseModel):
    v: Optional[bool] = False
    link: Optional[bool] = False
    force: Optional[bool] = False

class VolumeCreateRequest(BaseModel):
    name: Optional[str] = None
    driver: Optional[str] = None
    driver_opts: Optional[Dict[str, Any]] = None
    labels: Optional[Dict[str, str]] = None

class VolumeRemoveRequest(BaseModel):
    force: Optional[bool] = False