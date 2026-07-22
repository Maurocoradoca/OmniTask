from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.presentation.tasks import router as tasks_router
from app.presentation.schedules import router as schedules_router
from app.presentation.analytics import router as analytics_router
from app.infrastructure.database import engine, Base
from app.infrastructure import models

Base.metadata.create_all(bind=engine)

def create_app() -> FastAPI:
    """Fábrica de la aplicación FastAPI."""
    app = FastAPI(
        title="Student Life Manager API",
        description="API para el asistente personal inteligente.",
        version="0.5.0" 
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"], 
        allow_credentials=True,
        allow_methods=["*"], 
        allow_headers=["*"],
    )

    app.include_router(tasks_router)  # Incluimos el router de tareas en nuestra aplicación
    app.include_router(schedules_router)  # Incluimos el router de horarios en nuestra aplicación
    app.include_router(analytics_router)  # Incluimos el router de análisis en nuestra aplicación

    @app.get("/", tags=["Health Check"])
    def read_root():
        return {
            "status": "online",
            "message": "¡Bienvenido al backend de tu Asistente Personal!"
        }

    return app

app = create_app()