from fastapi import FastAPI
from scripts.services.service import router

app = FastAPI(root_path="/ems")
app.include_router(router)
