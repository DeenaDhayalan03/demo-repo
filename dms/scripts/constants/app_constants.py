from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_409_CONFLICT,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_503_SERVICE_UNAVAILABLE,
)

NOT_FOUND_ERROR = {"message": "The requested resource was not found.", "status": HTTP_404_NOT_FOUND}
INTERNAL_SERVER_ERROR = {"message": "An internal server error occurred.", "status": HTTP_500_INTERNAL_SERVER_ERROR}

AUTH_SUCCESS = {"message": "Authentication successful.", "status": HTTP_200_OK}
AUTH_FAILURE = {"message": "Authentication failed. Invalid credentials.", "status": HTTP_401_UNAUTHORIZED}
AUTH_LOGOUT_SUCCESS = {"message": "Logged out successfully.", "status": HTTP_200_OK}
AUTH_REQUIRED = {"message": "Authentication required before performing this action.", "status": HTTP_401_UNAUTHORIZED}


IMAGE_BUILD_SUCCESS = {"message": "Docker image built successfully.", "status": HTTP_201_CREATED}
IMAGE_BUILD_FAILURE = {"message": "Failed to build Docker image.", "status": HTTP_400_BAD_REQUEST}
IMAGE_PUSH_SUCCESS = {"message": "Docker image pushed successfully.", "status": HTTP_200_OK}
IMAGE_PUSH_FAILURE = {"message": "Failed to push Docker image to registry.", "status": HTTP_400_BAD_REQUEST}
IMAGE_PULL_SUCCESS = {"message": "Docker image pulled successfully.", "status": HTTP_200_OK}
IMAGE_PULL_FAILURE = {"message": "Failed to pull Docker image from registry.", "status": HTTP_400_BAD_REQUEST}
IMAGE_REMOVE_SUCCESS = {"message": "Docker image removed successfully.", "status": HTTP_200_OK}
IMAGE_REMOVE_FAILURE = {"message": "Failed to remove Docker image.", "status": HTTP_400_BAD_REQUEST}
IMAGE_NOT_FOUND = {"message": "Requested image not found.", "status": HTTP_404_NOT_FOUND}
IMAGE_LIST_RETRIEVED = {"message": "List of Docker images retrieved successfully.", "status": HTTP_200_OK}
IMAGE_DELETE_SUCCESS = {"message": "Docker image deleted successfully.", "status": HTTP_200_OK}
IMAGE_LIST_SUCCESS = {"message": "Docker image listed successfully.", "status": HTTP_200_OK}


CONTAINER_CREATE_SUCCESS = {"message": "Docker container created successfully.", "status": HTTP_201_CREATED}
CONTAINER_CREATE_FAILURE = {"message": "Failed to create Docker container.", "status": HTTP_400_BAD_REQUEST}
CONTAINER_STOP_SUCCESS = {"message": "Docker container stopped successfully.", "status": HTTP_200_OK}
CONTAINER_STOP_FAILURE = {"message": "Failed to stop Docker container.", "status": HTTP_400_BAD_REQUEST}
CONTAINER_RESTART_SUCCESS = {"message": "Docker container restarted successfully.", "status": HTTP_200_OK}
CONTAINER_RESTART_FAILURE = {"message": "Failed to restart Docker container.", "status": HTTP_400_BAD_REQUEST}
CONTAINER_REMOVE_SUCCESS = {"message": "Docker container removed successfully.", "status": HTTP_200_OK}
CONTAINER_REMOVE_FAILURE = {"message": "Failed to remove Docker container.", "status": HTTP_400_BAD_REQUEST}
CONTAINER_LOGS_RETRIEVED = {"message": "Docker container logs retrieved successfully.", "status": HTTP_200_OK}
CONTAINER_LOGS_FAILURE = {"message": "Failed to retrieve Docker containers.", "status": HTTP_400_BAD_REQUEST}
CONTAINER_LOGS_NOT_FOUND = {"message": "Requested container logs not found.", "status": HTTP_404_NOT_FOUND}
CONTAINER_NOT_FOUND = {"message": "Requested container not found.", "status": HTTP_404_NOT_FOUND}
CONTAINER_LIST_RETRIEVED = {"message": "List of Docker containers retrieved successfully.", "status": HTTP_200_OK}


VOLUME_CREATE_SUCCESS = {"message": "Docker volume created successfully.", "status": HTTP_201_CREATED}
VOLUME_CREATE_FAILURE = {"message": "Failed to create Docker volume.", "status": HTTP_400_BAD_REQUEST}
VOLUME_REMOVE_SUCCESS = {"message": "Docker volume removed successfully.", "status": HTTP_200_OK}
VOLUME_REMOVE_FAILURE = {"message": "Failed to remove Docker volume.", "status": HTTP_400_BAD_REQUEST}
VOLUME_NOT_FOUND = {"message": "Requested volume not found.", "status": HTTP_404_NOT_FOUND}
VOLUME_LIST_SUCCESS = {"message": "Requested volume retrieved successfully.", "status": HTTP_200_OK}
VOLUME_LIST_FAILURE = {"message": "Requested volume not retrieved.", "status": HTTP_400_BAD_REQUEST}
VOLUME_LIST_RETRIEVED = {"message": "List of Docker volumes retrieved successfully.", "status": HTTP_200_OK}
VOLUME_RETRIEVE_FAILURE = {"message": "Volume retrieval failed.", "status": HTTP_400_BAD_REQUEST}


COMPOSE_UP_SUCCESS = {"message": "Docker Compose services started successfully.", "status": HTTP_200_OK}
COMPOSE_UP_FAILURE = {"message": "Failed to start Docker Compose services.", "status": HTTP_400_BAD_REQUEST}
COMPOSE_DOWN_SUCCESS = {"message": "Docker Compose services stopped successfully.", "status": HTTP_200_OK}
COMPOSE_DOWN_FAILURE = {"message": "Failed to stop Docker Compose services.", "status": HTTP_400_BAD_REQUEST}
COMPOSE_LOGS_RETRIEVED = {"message": "Docker Compose logs retrieved successfully.", "status": HTTP_200_OK}
COMPOSE_STATUS_RETRIEVED = {"message": "Docker Compose service status retrieved successfully.", "status": HTTP_200_OK}


PRUNE_IMAGES_SUCCESS = {"message": "Unused Docker images removed successfully.", "status": HTTP_200_OK}
PRUNE_CONTAINERS_SUCCESS = {"message": "Stopped Docker containers removed successfully.", "status": HTTP_200_OK}
PRUNE_VOLUMES_SUCCESS = {"message": "Unused Docker volumes removed successfully.", "status": HTTP_200_OK}
PRUNE_SYSTEM_SUCCESS = {"message": "System prune completed successfully.", "status": HTTP_200_OK}
PRUNE_IMAGES_FAILURE = {"message": "Failed to remove unused Docker images.", "status": HTTP_500_INTERNAL_SERVER_ERROR}
PRUNE_CONTAINERS_FAILURE = {"message": "Failed to remove stopped Docker containers.", "status": HTTP_500_INTERNAL_SERVER_ERROR}
PRUNE_VOLUMES_FAILURE = {"message": "Failed to remove unused Docker volumes.", "status": HTTP_500_INTERNAL_SERVER_ERROR}
PRUNE_SYSTEM_FAILURE = {"message": "System prune operation failed.", "status": HTTP_500_INTERNAL_SERVER_ERROR}
PRUNE_SERVICE_ERROR = {"message": "Error occurred in the prune service.", "status": HTTP_500_INTERNAL_SERVER_ERROR}
PRUNE_API_ERROR = {"message": "Error occurred in the prune API.", "status": HTTP_500_INTERNAL_SERVER_ERROR}


STATUS_OK = {"message": "Request processed successfully.", "status": HTTP_200_OK}
STATUS_CREATED = {"message": "Resource created successfully.", "status": HTTP_201_CREATED}
STATUS_BAD_REQUEST = {"message": "Invalid request parameters.", "status": HTTP_400_BAD_REQUEST}
STATUS_UNAUTHORIZED = {"message": "Unauthorized access. Please authenticate.", "status": HTTP_401_UNAUTHORIZED}
STATUS_FORBIDDEN = {"message": "Permission denied for this operation.", "status": HTTP_403_FORBIDDEN}
STATUS_NOT_FOUND = {"message": "Requested resource not found.", "status": HTTP_404_NOT_FOUND}
STATUS_CONFLICT = {"message": "Request conflicts with existing data.", "status": HTTP_409_CONFLICT}
STATUS_INTERNAL_ERROR = {"message": "An unexpected error occurred. Please try again.", "status": HTTP_500_INTERNAL_SERVER_ERROR}
STATUS_SERVICE_UNAVAILABLE = {"message": "Service is temporarily unavailable. Please try again later.", "status": HTTP_503_SERVICE_UNAVAILABLE}


INVALID_REQUEST = {"message": "Invalid request parameters.", "status": HTTP_400_BAD_REQUEST}
INTERNAL_SERVER_ERROR = {"message": "An unexpected error occurred. Please try again.", "status": HTTP_500_INTERNAL_SERVER_ERROR}
DOCKER_DAEMON_UNAVAILABLE = {"message": "Docker daemon is unavailable or not running.", "status": HTTP_503_SERVICE_UNAVAILABLE}
PERMISSION_DENIED = {"message": "Permission denied for this operation.", "status": HTTP_403_FORBIDDEN}
ACTION_FAILED = {"message": "Action could not be completed.", "status": HTTP_400_BAD_REQUEST}
