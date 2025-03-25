import os
from dotenv import load_dotenv

load_dotenv(".env")


class AppConfig:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///app_data/files.db")
    API_HOST = os.getenv("API_HOST", "127.0.0.1")
    API_PORT = int(os.getenv("API_PORT", "8000"))
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "upload_directory")

    @staticmethod
    def init_directories():
        os.makedirs(AppConfig.UPLOAD_FOLDER, exist_ok=True)  # Improved directory creation


# Initialize directories at import
AppConfig.init_directories()
