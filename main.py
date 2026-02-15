from fastapi import FastAPI
import uvicorn
from cadastro import SistemaGerenciamento
from usuario import Usuario

app = FastAPI()

sistema = SistemaGerenciamento();

@app.get("/sistema-cadastro")
def exibir_listas():
    return sistema.listar_usuarios();

@app.post("/sistema-cadastro")
def criar_usuario(usuario: Usuario):
    sistema.cadastrar_usuario(usuario)
    return {"mensagem: Usuário cadastrado!"}

@app.delete("/sistema-cadastro/{id_usuario}")
def remover_usuario(id_usuario: int):
    removido = sistema.remover_usuario(id_usuario);

    if not removido:
        raise Exception(status_code = 404, detail="Usuario não encontrado!")
    return {"mensagem: Usuário removido com sucesso!"}