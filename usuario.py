from pydantic import BaseModel
class Usuario(BaseModel):
    def __init__(self, id_usuario, nome, idade, email):
        self.id = id_usuario;
        self.nome = nome;
        self.idade = idade;
        self.email = email;
