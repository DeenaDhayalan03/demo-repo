import subprocess
from fastapi import HTTPException
from scripts.constants.app_constants import (
    COMPOSE_UP_SUCCESS, COMPOSE_UP_FAILURE,
    COMPOSE_DOWN_SUCCESS, COMPOSE_DOWN_FAILURE,
    COMPOSE_LOGS_RETRIEVED, COMPOSE_STATUS_RETRIEVED
)
from scripts.models.compose_model import ComposeUpRequest, ComposeDownRequest, ComposeLogsRequest, ComposeStatusRequest


def run_compose_command(command: str, compose_file_path: str) -> str:
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
            status_code=400,
            detail=f"Error occurred while running command: {e.stderr.decode('utf-8')}"
        )


def compose_up(compose_request: ComposeUpRequest) -> dict:
    compose_file_path = compose_request.compose_file_path
    detach_option = "-d" if compose_request.detach else ""
    command = f"docker-compose -f {compose_file_path} up {detach_option}"

    output = run_compose_command(command, compose_file_path)

    if output:
        return {
            "message": COMPOSE_UP_SUCCESS["message"],
            "status": COMPOSE_UP_SUCCESS["status"],
            "output": output
        }
    else:
        raise HTTPException(
            status_code=COMPOSE_UP_FAILURE["status"],
            detail=COMPOSE_UP_FAILURE["message"]
        )


def compose_down(compose_request: ComposeDownRequest) -> dict:
    compose_file_path = compose_request.compose_file_path
    command = f"docker-compose -f {compose_file_path} down"

    output = run_compose_command(command, compose_file_path)

    if output:
        return {
            "message": COMPOSE_DOWN_SUCCESS["message"],
            "status": COMPOSE_DOWN_SUCCESS["status"],
            "output": output
        }
    else:
        raise HTTPException(
            status_code=COMPOSE_DOWN_FAILURE["status"],
            detail=COMPOSE_DOWN_FAILURE["message"]
        )


def retrieve_compose_logs(compose_request: ComposeLogsRequest) -> dict:
    compose_file_path = compose_request.compose_file_path
    command = f"docker-compose -f {compose_file_path} logs"

    output = run_compose_command(command, compose_file_path)

    if output:
        return {
            "message": COMPOSE_LOGS_RETRIEVED["message"],
            "status": COMPOSE_LOGS_RETRIEVED["status"],
            "output": output
        }
    else:
        raise HTTPException(
            status_code=400,
            detail=COMPOSE_LOGS_RETRIEVED["message"]  # Use app_constants for error message
        )


def retrieve_compose_status(compose_request: ComposeStatusRequest) -> dict:
    compose_file_path = compose_request.compose_file_path
    command = f"docker-compose -f {compose_file_path} ps --services"

    output = run_compose_command(command, compose_file_path)

    services = [{"name": service.strip(), "status": "running"} for service in output.splitlines()]

    if services:
        return {
            "message": COMPOSE_STATUS_RETRIEVED["message"],
            "status": COMPOSE_STATUS_RETRIEVED["status"],
            "services": services
        }
    else:
        raise HTTPException(
            status_code=400,
            detail=COMPOSE_STATUS_RETRIEVED["message"]  # Use app_constants for error message
        )
