from fastapi import FastAPI
from .database import engine, metadata
from .routers import usuarios 

# Crea la aplicación FastAPI
app = FastAPI()

# Crea las tablas si no existe
metadata.create_all(engine)

# Registra las rutas del ruter de usuarios
app.include_router(usuarios.router)