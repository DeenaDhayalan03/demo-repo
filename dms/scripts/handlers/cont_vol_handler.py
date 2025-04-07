from scripts.utils.cont_vol_utils import ContainerWithVolumeUtils
from scripts.models.cont_vol_model import (
    ContainerWithVolumeRequest, ContainerWithVolumeResponse,
    ContainerActionResponse, ContainerLogsResponse,
    VolumeDetailsResponse, VolumeListResponse, VolumeActionResponse
)
from fastapi import HTTPException
from scripts.constants import app_constants as constants
from scripts.logging.logger import logger


class ContainerWithVolumeHandler:
    def __init__(self):
        self.utils = ContainerWithVolumeUtils()


    def create_container_with_volume(self, request: ContainerWithVolumeRequest) -> ContainerWithVolumeResponse:
        try:
            response = self.utils.create_container_with_volume(request)
            logger.info(f"Container created: {response.container_id}, Volume: {response.volume_name}")
            return response
        except HTTPException as e:
            logger.error(f"{constants.CONTAINER_CREATE_FAILURE}: {e.detail}")
            raise e


    def start_container(self, container_id: str) -> ContainerActionResponse:
        try:
            response = self.utils.start_container(container_id)
            logger.info(f"Container started: {response.container_id}")
            return response
        except HTTPException as e:
            logger.error(f"{constants.CONTAINER_START_FAILURE}: {e.detail}")
            raise e


    def stop_container(self, container_id: str) -> ContainerActionResponse:
        try:
            response = self.utils.stop_container(container_id)
            logger.info(f"Container stopped: {response.container_id}")
            return response
        except HTTPException as e:
            logger.error(f"{constants.CONTAINER_STOP_FAILURE}: {e.detail}")
            raise e


    def get_container_logs(self, container_id: str) -> ContainerLogsResponse:
        try:
            response = self.utils.get_container_logs(container_id)
            logger.info(f"Logs retrieved for container: {container_id}")
            return response
        except HTTPException as e:
            logger.error(f"{constants.CONTAINER_LOGS_FAILURE}: {e.detail}")
            raise e


    def list_containers(self):
        try:
            response = self.utils.list_containers()
            logger.info("Container list retrieved")
            return response
        except HTTPException as e:
            logger.error(f"{constants.CONTAINER_LIST_FAILURE}: {e.detail}")
            raise e


    def get_container_details(self, container_id: str):
        try:
            response = self.utils.get_container_details(container_id)
            logger.info(f"Details fetched for container: {container_id}")
            return response
        except HTTPException as e:
            logger.error(f"{constants.CONTAINER_DETAILS_FAILURE}: {e.detail}")
            raise e


    def remove_container(self, container_id: str) -> ContainerActionResponse:
        try:
            response = self.utils.remove_container(container_id)
            logger.info(f"Container removed: {container_id}")
            return response
        except HTTPException as e:
            logger.error(f"{constants.CONTAINER_REMOVE_FAILURE}: {e.detail}")
            raise e


    def list_volumes(self) -> VolumeListResponse:
        try:
            response = self.utils.list_volumes()
            logger.info("Volume list retrieved")
            return response
        except HTTPException as e:
            logger.error(f"{constants.VOLUME_RETRIEVE_FAILURE}: {e.detail}")
            raise e


    def get_volume_details(self, volume_id: str) -> VolumeDetailsResponse:
        try:
            response = self.utils.get_volume_details(volume_id)
            logger.info(f"Volume details retrieved for: {volume_id}")
            return response
        except HTTPException as e:
            logger.error(f"{constants.VOLUME_RETRIEVE_FAILURE}: {e.detail}")
            raise e


    def remove_volume(self, volume_id: str) -> VolumeActionResponse:
        try:
            response = self.utils.remove_volume(volume_id)
            logger.info(f"Volume removed: {volume_id}")
            return response
        except HTTPException as e:
            logger.error(f"{constants.VOLUME_REMOVE_FAILURE}: {e.detail}")
            raise e
