# Nexus-Core API

API robusta y escalable construida con FastAPI siguiendo principios de Clean Architecture.

## Estructura del Proyecto 

```
Nexus-Core-API/
├── app/
│   ├── __init__.py
│   ├── main.py              # Punto de entrada
│   ├── core/                # Configuración y seguridad
│   │   ├── __init__.py
│   │   └── config.py
│   ├── api/                 # Endpoints y routers
│   │   ├── __init__.py
│   │   └── endpoints/
│   │       └── __init__.py
│   ├── models/              # Esquemas de datos (Pydantic)
│   │   └── __init__.py
│   └── services/            # Lógica de negocio
│       └── __init__.py
├── requirements.txt
└── README.md
```

## Instalación

1. Crear y activar entorno virtual:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución

```bash
uvicorn app.main:app --reload
```

La API estará disponible en: http://localhost:8000

## Documentación

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir qué te gustaría cambiar.

## 🎓 Créditos

Este proyecto implementa una **Clean Architecture** moderna.
* **Stack:** Python 3.10+, FastAPI.
* **Herramientas:** Cursor AI, Git.

---
*Desarrollado por Samuel Martinez* 🐵
