from pydantic import BaseModel, EmailStr
from uuid import UUID, uuid4

class UsuarioCreate(BaseModel):
    
    nome: str
    idade: int
    email: EmailStr
    
class UsuarioUpdate(BaseModel):
    nome: str
    idade: int
    email: EmailStr
    
class Usuario(BaseModel):
    id: UUID
    nome: str
    idade: int
    email: EmailStr