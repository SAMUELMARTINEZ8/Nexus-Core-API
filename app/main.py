"""
Punto de entrada principal de la aplicación FastAPI.
"""
from fastapi import FastAPI
from app.api.endpoints.users import router as user_router

app = FastAPI(
    title="Nexus-Core API",
    description="API robusta y escalable con arquitectura modular",
    version="1.0.0"
)

# Incluir routers
app.include_router(user_router, prefix="/api/v1", tags=["users"])


@app.get("/")
async def root():
    """Endpoint raíz que retorna un mensaje de bienvenida."""
    return {"message": "Hola Nexus-Core"}
