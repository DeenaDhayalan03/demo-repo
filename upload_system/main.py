from fastapi import FastAPI
from scripts.utils.db_utils import Base, engine
from scripts.services.upload_service import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI File Upload Service")

app.include_router(router)
