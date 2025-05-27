from .database import BASE
from sqlalchemy import Column, Integer, String, ForeignKey

#crear la base de modelo(entidad)
class Categoria(BASE):
    __tablename__= "categorias"
    id = Column(Integer,
                primary_key=True
                )
    nombre = Column(String(50))
class Productos(BASE):

    __tablename__="productos"
    id = Column(Integer, 
                primary_key=True)
    nombre = Column(String(40))
    modelo = Column(String(60))
    precio = Column(Integer)
    Categoria_id = Column(Integer,ForeignKey("categorias.id") )
