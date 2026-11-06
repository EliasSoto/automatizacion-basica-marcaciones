from api.base_de_datos import Base, engine
from api import entidades

Base.metadata.create_all(bind=engine)

print("Tablas creadas correctamente.")