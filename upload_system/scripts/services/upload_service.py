from fastapi import APIRouter, Depends, File, UploadFile, Form
from sqlalchemy.orm import Session
from scripts.utils.db_utils import SessionLocal
from scripts.handlers.upload_handler import save_uploaded_file, save_file_record, get_files_by_name
from scripts.logging.logger import logger

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/files/")
async def upload_file(name: str = Form(...), file: UploadFile = File(...), db: Session = Depends(get_db)):
    filename, file_path = save_uploaded_file(name, file)
    file_record = save_file_record(db, name, filename)

    logger.info(f"File uploaded: {file_record.filename}, stored at {file_record.file_path}")  # Log file upload
    return {"message": "File uploaded successfully", "file_id": file_record.id, "file_path": file_record.file_path}


@router.get("/files/{name}")
async def list_files(name: str, db: Session = Depends(get_db)):
    files = get_files_by_name(db, name)
    if not files:
        logger.warning(f"No files found for name: {name}")
        return {"message": "No files found"}

    logger.info(f"Files retrieved for name: {name}")
    return {"files": [{"id": file.id, "filename": file.filename, "file_path": file.file_path} for file in files]}
