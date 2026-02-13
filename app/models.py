from sqlalchemy import Table, Column, Integer, String
from .database import metadata

# Definición de la tabla
usuarios = Table(
    'usuarios', # Nombre de la tabla
    metadata, # Metadata donde se registrará la tabla
    #Columnas de la tabla 
    # El ID se incrementara con cada nuevo usuario
    Column('id_usuario',Integer, primary_key=True, autoincrement=True),
    # "nullable=Fase" = obligatorio rellenar campos 
    Column('nombre', String(20), nullable=True),
    Column('apellidos',String(50),nullable=False),
    Column('año_nacimiento', Integer, nullable=False)
)