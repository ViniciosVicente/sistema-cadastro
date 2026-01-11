class Usuario:
    def __init__(self, id_usuario, nome, idade, email):
        self.id = id_usuario;
        self.nome = nome;
        self.idade = idade;
        self.email = email;

class SistemaGerenciamento:
    def __init__(self):
        self.usuarios = []
        self.proximo_id = 1;
    
    def iniciar(self):
        while True:
            try:
                opcoes = int(input("--- SISTEMA DE CADASTRO ---\n\n1 - CADASTRAR USUÁRIO\n2 - VISUALIZAR CADASTROS\n3 - REMOVER CADASTRO\n4 - SAIR\n:"))
                if(opcoes == 1):
                    self.cadastrar_usuario();
                elif(opcoes == 2):
                    self.listar_usuarios();
                elif(opcoes == 3):
                    self.remover_usuario();
                elif(opcoes == 4):
                    break;
                else:
                    print("ERRO: Opção não existe!! Tente novamente")
                               
            except ValueError:
                print("ERRO: Valor inválido! Tente novamente ")
    
    def cadastrar_usuario(self,nome,idade,email):
       
        usuario = Usuario(self.proximo_id,nome,idade,email);
        self.proximo_id += 1
        self.usuarios.append(usuario)
        return usuario
            
    def listar_usuarios(self):
        return self.usuarios
        
    def remover_usuario(self):

        for contador, usuarios_listas in enumerate(self.usuarios):
            if usuarios_listas.id == self.id_usuario:
                self.usuarios.pop(contador)
                return True
            return False

