from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import usuarios

# Crea un router para agrupar las rutas relacionadas con usuarios
router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

# Dependencia que crea y cierra una sesión en la base de datos por petición
def get_db():
    db = SessionLocal()     #Abre la sesion
    try:
        yield db            #Devuelve la ruta solicitada(crear o listar de momento)
    finally:
        db.close()          #Se cierra al terminar la petición

#Creación de usuario
@router.post("/")
def crear_usuario(data: dict, db: Session= Depends(get_db)):
    # Construye una sentencia SQL INSERT con los datos recibidos
    query = usuarios.insert().values(data)
    # Ejecuta la sentencia en la base de datos
    db.execute(query)
    # Guarda los cambios
    db.commit()
    # Mensaje tranqulizador de todo OK
    return{"mensaje":"Usuario creado correctamente"}

# Listar usuarios
@router.get("/")
def listar_usuarios (db: Session= Depends(get_db)):
    # Construye una sentencia SELECT * FROM usuaraios (obtiene todo los datos de la tabla 'usuarios')
    query = usuarios.select()
    # Ejecuta la consulta y obtiene todos los registros
    resultado = db.execute(query).fetchall()
    # Convierto el resultado que esta en ROW a JSON
    usuarios_lista = [dict(row._mapping) for row in resultado] 
    # Devuelve los datos ahora en JSON
    return usuarios_lista