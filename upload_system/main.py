from fastapi import FastAPI
from scripts.utils.db_utils import Base, engine
from scripts.services.upload_service import router

Base.metadata.create_all(bind=engine)

app = FastAPI(root_path="/upload_system")

app.include_router(router)
