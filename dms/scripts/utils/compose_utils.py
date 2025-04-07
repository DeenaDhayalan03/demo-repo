import os
import subprocess
from typing import Optional
from fastapi import HTTPException
from scripts.models.compose_model import (
    ComposeUpRequest,
    ComposeDownRequest,
    ComposeActionResponse
)
from scripts.constants.app_constants import (
    COMPOSE_UP_SUCCESS, COMPOSE_DOWN_SUCCESS
)
from scripts.logging.logger import logger


class ComposeUtils:

    def _run_compose_command(self, command: list, cwd: Optional[str] = None) -> str:
        try:
            result = subprocess.run(
                command,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=cwd
            )
            return result.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            logger.error(f"Command failed: {' '.join(command)} -> {e.stderr.decode('utf-8')}")
            raise HTTPException(
                status_code=400,
                detail=f"Command execution failed: {e.stderr.decode('utf-8')}"
            )

    def compose_up(self, request: ComposeUpRequest) -> ComposeActionResponse:
        detach_option = "-d" if request.detach else ""
        compose_dir = os.path.dirname(request.compose_file_path)
        command = ["docker", "compose", "-f", request.compose_file_path, "up"]
        if detach_option:
            command.append(detach_option)

        output = self._run_compose_command(command, cwd=compose_dir)
        logger.info(f"Docker Compose UP executed: {request.compose_file_path}")
        return ComposeActionResponse(
            message=COMPOSE_UP_SUCCESS,
            output=output
        )

    def compose_down(self, request: ComposeDownRequest) -> ComposeActionResponse:
        compose_dir = os.path.dirname(request.compose_file_path)
        command = ["docker", "compose", "-f", request.compose_file_path, "down"]

        output = self._run_compose_command(command, cwd=compose_dir)
        logger.info(f"Docker Compose DOWN executed: {request.compose_file_path}")
        return ComposeActionResponse(
            message=COMPOSE_DOWN_SUCCESS,
            output=output
        )
