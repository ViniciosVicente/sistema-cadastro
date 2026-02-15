from usuario import Usuario

class SistemaGerenciamento:
    def __init__(self):
        self.lista_usuarios = []
        
    def cadastrar_usuario(self, usuario):
        self.lista_usuarios.append(usuario)
        
    def listar_usuarios(self):
        return self.lista_usuarios
        
    def remover_usuario(self, id_usuario):

        for contador, usuarios_listas in enumerate(self.lista_usuarios):
            if usuarios_listas.id == id_usuario:
                self.lista_usuarios.pop(contador)
                return True
        return False



