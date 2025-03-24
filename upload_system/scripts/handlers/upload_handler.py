import os
from fastapi import UploadFile
from sqlalchemy.orm import Session
from scripts.models.database_model import UploadedFile
from scripts.constants.app_configuration import AppConfig
from scripts.logging.logger import logger

UPLOAD_FOLDER = AppConfig.UPLOAD_FOLDER


def save_file_record(db: Session, name: str, filename: str):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file_record = UploadedFile(name=name, filename=filename, file_path=file_path)
    db.add(file_record)
    db.commit()
    db.refresh(file_record)

    logger.info(f"File record saved: {file_record}")
    return file_record


def get_files_by_name(db: Session, name: str):
    return db.query(UploadedFile).filter(UploadedFile.name == name).all()
    logger.info(f"Retrieved {len(files)} files for name: {name}")  # Log retrieval


def save_uploaded_file(name: str, file: UploadFile):
    filename = f"{name}_{file.filename}"
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return filename, file_path
