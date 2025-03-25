from sqlalchemy import Column, Integer, String
from scripts.utils.db_utils import Base


class UploadedFile(Base):
    __tablename__ = "uploaded_files"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    filename = Column(String, unique=True, index=True)
    file_path = Column(String, unique=True, index=True)
