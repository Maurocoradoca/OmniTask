from fastapi import FastAPI

def create_app() -> FastAPI:
    """Fábrica de la aplicación FastAPI."""
    app = FastAPI(
        title="Student Life Manager API",
        description="API para el asistente personal inteligente.",
        version="0.5.0" 
    )

    @app.get("/", tags=["Health Check"])
    def read_root():
        return {
            "status": "online",
            "message": "¡Bienvenido al backend de tu Asistente Personal!"
        }

    return app

app = create_app()