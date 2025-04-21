from pymongo import MongoClient
from scripts.constants.app_configuration import settings
import logging

logger = logging.getLogger(__name__)

class MongoDBConnection:
    def __init__(self):
        self.client = MongoClient(settings.MONGODB_URI)
        self.db = self.client[settings.MONGODB_DATABASE]
