from fastapi import FastAPI, Depends
import uvicorn
from cadastro import SistemaGerenciamento
from usuario import Usuario, UsuarioCreate, UsuarioUpdate
from uuid import UUID
from database import SessionLocal, engine
import models
from sqlalchemy.orm import Session
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

sistema = SistemaGerenciamento();

# função para criar uma conexão com o banco

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/Sistema-cadastro")
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(models.UsuarioDB).all()
    return {f"mensagem: Usuários listados"}

@app.post("/Sistema-cadastro")
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    
    novo_usuario = models.UsuarioDB(nome=usuario.nome,idade=usuario.idade, email=usuario.email)
    
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    
    return {f"mensagem: Usuário cadastrado!"}

@app.put("/Sistema-cadastro")
def atualizar_usuario(usuario: UsuarioUpdate,id, db: Session = Depends(get_db)):
    
    usuario_atualizado = models.UsuarioDB(nome=usuario.nome,idade=usuario.idade, email=usuario.email)
    
    if not usuario_atualizado:
        raise Exception(status_code = 404, detail="Usuário não encontrado!")
    return {f"Usuário atualizado!"}