"""
Modelo de usuario usando Pydantic.
"""
from pydantic import BaseModel


class User(BaseModel):
    """Modelo de usuario con validación de datos."""
    
    id: int
    username: str
    email: str
    role: str = "user"
    
    class Config:
        """Configuración del modelo."""
        json_schema_extra = {
            "example": {
                "id": 1,
                "username": "johndoe",
                "email": "john.doe@example.com",
                "role": "user"
            }
        }
