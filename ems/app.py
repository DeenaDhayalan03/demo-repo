from fastapi import FastAPI
from scripts.services.service import router

app = FastAPI()
app.include_router(router)
