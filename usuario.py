from pydantic import BaseModel, EmailStr
from uuid import UUID, uuid4

class UsuarioCreate(BaseModel):
    
    nome: str
    idade: int
    email: EmailStr
class UsuarioUpdate:
    nome: str
    idade: str
    email: EmailStr
class Usuario(BaseModel):
    id: UUID
    nome: str
    idade: int
    email: EmailStr