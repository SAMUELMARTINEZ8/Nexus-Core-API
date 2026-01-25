"""
Endpoints relacionados con usuarios.
"""
from fastapi import APIRouter
from typing import List
from app.models.user import User
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["users"])


class UserCreate(BaseModel):
    """Modelo para crear un nuevo usuario (sin id)."""
    username: str
    email: str
    role: str = "user"


@router.get("", response_model=List[User])
async def get_users():
    """
    Obtiene una lista de usuarios.
    
    Returns:
        List[User]: Lista de usuarios falsos.
    """
    # Lista de 3 usuarios falsos
    fake_users = [
        User(id=1, username="johndoe", email="john.doe@example.com", role="user"),
        User(id=2, username="janedoe", email="jane.doe@example.com", role="admin"),
        User(id=3, username="bobsmith", email="bob.smith@example.com", role="user")
    ]
    return fake_users


@router.post("", response_model=User, status_code=201)
async def create_user(user: UserCreate):
    """
    Crea un nuevo usuario.
    
    Args:
        user: Datos del usuario a crear.
    
    Returns:
        User: Usuario creado con id asignado.
    """
    # Simulando la creación: asignamos un id ficticio
    new_user = User(
        id=999,  # En producción, esto vendría de la base de datos
        username=user.username,
        email=user.email,
        role=user.role
    )
    return new_user
