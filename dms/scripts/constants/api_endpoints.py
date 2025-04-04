IMAGE_BUILD = "/docker/images"
IMAGE_PUSH = "/docker/images/{image_id}/push"
IMAGE_PULL = "/docker/images/{image_id}/pull"
IMAGE_LIST = "/docker/images"
IMAGE_DETAILS = "/docker/images/{image_id}"
IMAGE_DELETE = "/docker/images/{image_id}"


CONTAINER_CREATE = "/docker/containers"
CONTAINER_STOP = "/docker/containers/{container_id}/stops"
CONTAINER_RESTART = "/docker/containers/{container_id}/restarts"
CONTAINER_LOGS = "/docker/containers/{container_id}/logs"
CONTAINER_LIST = "/docker/containers"
CONTAINER_DETAILS = "/docker/containers/{container_id}"
CONTAINER_DELETE = "/docker/containers/{container_id}"


VOLUME_CREATE = "/docker/volumes"
VOLUME_LIST = "/docker/volumes"
VOLUME_DETAILS = "/docker/volumes/{volume_id}"
VOLUME_DELETE = "/docker/volumes/{volume_id}"


COMPOSE_UP = "/docker/compose/up"
COMPOSE_STATUS = "/docker/compose"
COMPOSE_DOWN = "/docker/compose/down"
COMPOSE_LOGS = "/docker/compose/logs"


PRUNE_IMAGES = "/docker/images/prune"
PRUNE_CONTAINERS = "/docker/containers/prune"
PRUNE_VOLUMES = "/docker/volumes/prune"
PRUNE_ALL = "/docker/prune"
