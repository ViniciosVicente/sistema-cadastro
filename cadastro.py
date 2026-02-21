from usuario import Usuario
from uuid import uuid4, UUID
class SistemaGerenciamento:
    def __init__(self):
        self.lista_usuarios = []
        
    def cadastrar_usuario(self, dados_usuario):
        novo_usuario = Usuario(
            id=uuid4(),
            nome=dados_usuario.nome,
            idade=dados_usuario.idade,
            email=dados_usuario.email
        )
        self.lista_usuarios.append(novo_usuario);
    def exibir_usuarios(self):
        return self.lista_usuarios
    
    def atualizar_usuario(self, id_usuario: UUID, dados_atualizados):
        
        for usuario in self.lista_usuarios:
            if usuario.id == id_usuario:
                usuario.nome = dados_atualizados.nome,
                usuario.idade = dados_atualizados.idade,
                usuario.email = dados_atualizados.email
                return usuario
        return None
        
    def remover_usuario(self, id_usuario: UUID):

        for contador, usuarios_listas in enumerate(self.lista_usuarios):
            if usuarios_listas.id == id_usuario:
                self.lista_usuarios.pop(contador)
                return True
        return False



