from sqlalchemy import insert, MetaData, Table

# Importo la conexión y la tabla
from models import engine, usuarios

# Lista de usuarios a insertar
nuevos_usuarios = [
    {"nombre":"Abc","apellidos":"periodico","año_nacimiento":1990},
    {"nombre":"Manolo","apellidos":"prejubilado","año_nacimiento":1960},
    {"nombre":"Austero","apellidos":"Bermejales","año_nacimiento":1900},
]

# insertar en la base de datos
with engine.connect() as conn:
    conn.execute(usuarios.insert(), nuevos_usuarios)
    conn.commit()

# Mensaje tranquilizador
print("Usuarios insertados correctamente")