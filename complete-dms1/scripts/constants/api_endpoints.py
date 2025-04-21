class Endpoints:

    AUTH_SIGNUP = "/auth/signup"
    AUTH_LOGIN = "/auth/login"
    AUTH_LOGOUT = "/auth/logout"

    RATE_LIMIT_GET = "/rate-limit/{user_id}"
    RATE_LIMIT_SET = "/rate-limit/{user_id}/set"
    RATE_LIMIT_UPDATE = "/rate-limit/{user_id}/update"

    IMAGE_BUILD_ADV = "/docker/images/build"
    IMAGE_GITHUB_BUILD = "/docker/images/github-build"
    DOCKER_LOGIN = "/docker/login"
    IMAGE_PUSH = "/docker/images/push"
    IMAGE_PULL = "/docker/images/pull"
    IMAGE_LIST = "/docker/images/list"
    IMAGE_DETAILS = "/docker/images/details/{image_id}"
    IMAGE_DELETE = "/docker/images/delete/{image_id}"

    CONTAINER_RUN = "/docker/containers"
    CONTAINER_RUN_ADV = "/docker/containers/advanced"
    CONTAINER_START = "/docker/containers/{name}/start"
    CONTAINER_STOP = "/docker/containers/{name}/stop"
    CONTAINER_LOGS = "/docker/containers/{name}/logs"
    CONTAINER_LIST = "/docker/containers"
    CONTAINER_DETAILS = "/docker/containers/{name}"
    CONTAINER_REMOVE = "/docker/containers/{name}"

    VOLUME_CREATE = "/docker/volumes/create"
    VOLUME_DELETE = "/docker/volumes/delete/{name}"
    VOLUME_LIST = "/docker/volumes/list"
    VOLUME_DETAILS = "/docker/volumes/details/{name}"
