from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import cadastro

app = FastAPI()
sistema = cadastro.SistemaGerenciamento()


class UsuarioEntrada():
    nome: str
    idade: int
    email: str
    
@app.get("/cadastro")
def read_cadastro(cadastro_):
    return {"Hello": "Word"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")