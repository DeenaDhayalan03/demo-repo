from scripts.utils.image_utils import ImageUtils
from scripts.models.image_model import (
    ImageBuildRequest, ImagePushRequest, ImagePullRequest, ImageIDRequest
)
from scripts.constants.app_constants import (
    IMAGE_BUILD_SUCCESS, IMAGE_PUSH_SUCCESS, IMAGE_PULL_SUCCESS, IMAGE_DELETE_SUCCESS, IMAGE_LIST_SUCCESS
)

class ImageHandler:
    def __init__(self):
        self.image_utils = ImageUtils()

    def build_image(self, request: ImageBuildRequest):
        response = self.image_utils.build_image(request)
        return {**IMAGE_BUILD_SUCCESS, "image_id": response.image_id}

    def push_image(self, request: ImagePushRequest):
        response = self.image_utils.push_image(request)
        return {**IMAGE_PUSH_SUCCESS, "repository": response.repository}

    def pull_image(self, request: ImagePullRequest):
        response = self.image_utils.pull_image(request)
        return {**IMAGE_PULL_SUCCESS, "repository": response.repository}

    def list_images(self):
        response = self.image_utils.list_images()
        return {**IMAGE_LIST_SUCCESS, "images": response.images}

    def get_image_by_id(self, image_id: str):
        response = self.image_utils.get_image_by_id(image_id)
        return {"message": "Image details retrieved successfully.", "image": response}

    def delete_image(self, request: ImageIDRequest):
        response = self.image_utils.delete_image(request)
        return {**IMAGE_DELETE_SUCCESS, "image_id": response.image_id}
