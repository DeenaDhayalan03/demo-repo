from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from scripts.services.image_service import router as image_router
from scripts.services.cont_vol_service import router as cont_vol_router
from scripts.services.compose_service import router as compose_router

def create_app() -> FastAPI:
    app = FastAPI(
        title="Docker Management API",
        description="APIs to manage Docker images, containers, volumes, prune, and compose services",
        version="1.0.0"
    )

    # Enable CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(image_router, prefix="/image", tags=["Image Operations"])
    app.include_router(cont_vol_router, prefix="/container_volume", tags=["Container & Volume Operations"])
    app.include_router(compose_router, prefix="/compose", tags=["Docker Compose Operations"])

    return app
