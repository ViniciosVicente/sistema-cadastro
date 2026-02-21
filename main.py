from fastapi import FastAPI
import uvicorn
from cadastro import SistemaGerenciamento
from usuario import Usuario, UsuarioCreate, UsuarioUpdate
from uuid import UUID

app = FastAPI()

sistema = SistemaGerenciamento();

@app.get("/sistema-cadastro")
def exibir_listas():
    return sistema.exibir_usuarios();

@app.post("/sistema-cadastro")
def criar_usuario(usuario: UsuarioCreate):
    sistema.cadastrar_usuario(usuario)
    return {"mensagem: Usuário cadastrado!"}

@app.put("/sistema-cadastro/{id_usuario}")
def usuario_atualizado(id_usuario: UUID, usuario: UsuarioUpdate):
    update_dados = sistema.atualizar_usuario(id_usuario, usuario);
    
    if not update_dados:
        raise Exception(status_code = 404, detail="Usuário não encontrado!")
    return {"mensagem: Usuário atualizado com sucesso!"}
    
@app.delete("/sistema-cadastro/{id_usuario}")
def remover_usuario(id_usuario: UUID):
    removido = sistema.remover_usuario(id_usuario);

    if not removido:
        raise Exception(status_code = 404, detail="Usuario não encontrado!")
    return {"mensagem: Usuário removido com sucesso!"}