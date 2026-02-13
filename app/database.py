from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

# Datos de la conexión
usuario = "root"
contraseña = ""
host = "localhost"
nombre_bd = "prueba"

# Cadena de conexión para SQLAlchemy usando el driver PyMySQL
DATABASE_URL = f"mysql+pymysql://{usuario}:{contraseña}@{host}/{nombre_bd}"

# Crea el motor de conexión (engine) que gestiona la comunicación con MySQL
engine = create_engine(DATABASE_URL)
# Objeto que almacena la estructura de las tablas
metadata = MetaData()

# Crea una fábrica de sesiones para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)