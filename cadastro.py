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
    
    def cadastrar_usuario(self):
        print("--- CADASTRO USUÁRIO --- ")
        
        while True:
            
            while True:
                try:
                    nome = str(input("\nNome:"));
                    if not nome:
                        print("ERRO: Nome usuário não pode ser vazio!! Tente novamente");
                    else:
                        break;
                except ValueError:
                    print("ERRO: Valor nome inválido! Tente novamente")  
                
                
            while True:
                try:        
                    idade = int(input("Idade:"));
                    if (idade < 0):
                        print("ERRO: idade usuário não pode ser negativa!! Tente novamente");
                    else:
                        break;   
                except ValueError:
                    print("ERRO: Valor idade inválido! Tente novamente");
            
            while True:
                try:
                    email = input("Email:");
                    if '@'not in email or '.' not in email:
                        print("ERRO: Email inválido");
                    else:
                        break;
                except ValueError:
                    print("ERRO: Valor email inválido! Tente novamente")
            
            usuario = Usuario(self.proximo_id,nome,idade,email);
            self.proximo_id += 1
            self.usuarios.append(usuario)
                
            print("Usuário cadastrado!\n\n")
            self.cadastrar_novamente = int(input("Deseja cadastrar outro usuário?\n\n1 - Novo usuário\n2 - Sair\n:"));
            
            if(self.cadastrar_novamente == 1):
                continue
            elif(self.cadastrar_novamente == 2):
                break;
            
    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
            return
        
        while True:
            print("---USUÁRIOS CADASTRADOS---\n")
            print();
            for usuario_lista in self.usuarios:
                    print("--" * 10);
                    print(f"ID: {usuario_lista.id}\nNome: {usuario_lista.nome}\nIdade: {usuario_lista.idade}\nEmail: {usuario_lista.email}\n");
            
            try:    
                opcoes_visualizar = int(input("Deseja sair?\n\n1 - Visualizar novamente\n2 - Sair\n:"));
                if(opcoes_visualizar == 1):
                        continue
                elif(opcoes_visualizar == 2):
                        break;
                else:
                        print("Digito não corresponde as opções! Digite novamente.\n")
            except ValueError:
                    print("ERRO: Valor incorreto! Digite Novamente\n")
        
    def remover_usuario(self):
        print("---Remover usuário---\n")
        while True:
                if not self.usuarios:
                    print("Nenhum usuário cadastrado.")
                    return
                for usuario_remover in self.usuarios:
                        print(f"\nID: {usuario_remover.id}\nNome: {usuario_remover.nome}\n");
                        
                try:
                        id_remover = int(input("Digite o ID do usuário que deseja remover: "));
                        usuario_antes = len(self.usuarios);

                        for contador, usuarios_listas in enumerate(self.usuarios):
                            if usuarios_listas.id == id_remover:
                                self.usuarios.pop(contador)
                                break;        
            
                        if len(self.usuarios) < usuario_antes:    
                            print(f"\nUsuário {id_remover} removido!!\n")
                        else:
                            print(f"\nERRO: Usuário com ID {id_remover} não foi encontrado!")
                except ValueError:
                        print("ERRO: Digite um valor válido de ID\n")
                            
                try:
                    opcoes_remover = int(input("\nDeseja sair?\n1 - Remover outro usuário\n2 - Sair\n:"))
                    if(opcoes_remover == 1):
                        continue
                    elif(opcoes_remover == 2):
                        break;
                    else: 
                        print("\nERRO: Valor não corresponde às opções! Digite novamente.\n");
                except ValueError:
                                print("\nERRO: Valor incorreto! Digite Novamente\n")


sistema = SistemaGerenciamento()
sistema.iniciar()