import os
from dotenv import load_dotenv

load_dotenv(".env")


class AppConfig:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///files.db")
    API_HOST = os.getenv("API_HOST", "127.0.0.1")
    API_PORT = int(os.getenv("API_PORT", "8000"))
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "upload_directory")

    @staticmethod
    def init_directories():
        if not os.path.exists(AppConfig.UPLOAD_FOLDER):
            os.makedirs(AppConfig.UPLOAD_FOLDER)

AppConfig.init_directories()
