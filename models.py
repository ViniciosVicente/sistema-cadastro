import uuid
from sqlalchemy import Column, String, Integer
from database import Base

class UsuarioDB(Base):
    __tablename__ = "usuarios"
    
    id = Column(String, primary_key= True, default=lambda: str(uuid.uuid4()))
    nome = Column(String)
    idade = Column(Integer)
    email = Column(String)
    senha = Column(String)