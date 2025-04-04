from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from scripts.services.image_service import router as image_router
from scripts.services.container_service import router as container_router
from scripts.services.volume_service import router as volume_router
from scripts.services.prune_service import router as prune_router
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
    app.include_router(container_router, prefix="/container", tags=["Container Operations"])
    app.include_router(volume_router, prefix="/volume", tags=["Volume Operations"])
    app.include_router(prune_router, prefix="/prune", tags=["Prune Operations"])
    app.include_router(compose_router, prefix="/compose", tags=["Docker Compose Operations"])

    return app
