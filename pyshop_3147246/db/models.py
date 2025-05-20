from .database import BASE
from sqlalchemy import Column, Integer, String

#crear la base de modelo(entidad)
class Categoria(BASE):
    __tablename__= "categorias"
    id = Column(Integer,
                primary_key=True
                )
    nombre = Column(String(50))