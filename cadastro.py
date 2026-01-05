
dados_usuario = {};
dados_usuario_lista = [];
def sistema():
    
    while True:
        print("\n--Sistema de Cadastramento--\n");
        try:
            opcoes = int(input("Opções:\n1 - Cadastrar usuário\n2 - Usuários cadastrados\n3 - Remove usuário cadastrado\n4 - Sair\n:"));
            if(opcoes == 1):
                cadastrar_usuario();
            elif(opcoes == 2):
                listar_usuarios();
            elif(opcoes == 3): 
                remover_usuario();
            elif(opcoes == 4):
                break;
            else:
                print("Número digitado não corresponde as opções. Digite novamente!\n");         
        except ValueError:
            print("ERRO: Valor inválido! Digite novamente\n")
def gerar_novo_id():
    maior_id = 0;
    
    for usuario_gerarID in dados_usuario_lista:
        if(usuario_gerarID['id'] > maior_id):
            maior_id = usuario_gerarID['id'];
    return maior_id + 1;
def cadastrar_usuario():
    
    print("--- CADASTRO USUÁRIO ---\n")
    while True:
        id_usuario = gerar_novo_id()
        
        while True:
            try:
                nome_usuario = str(input("\nNome:"));
                if not nome_usuario:
                    print("ERRO: Nome usuário não pode ser vazio!! Tente novamente");
                else:
                    break;
            except ValueError:
                print("ERRO: Valor nome inválido! Tente novamente")        
           
        while True:        
            try:        
                idade_usuario = int(input("Idade:"));
                if (idade_usuario < 0):
                    print("ERRO: idade usuário não pode ser negativa!! Tente novamente");
                    if not idade_usuario:
                        print("ERRO: Idade usuário não pode ser vazio!! Tente novamente ")
                else:
                    break;   
            except ValueError:
                 print("ERRO: Valor idade inválido! Tente novamente");
        
        while True:
            try:
                email_usuario = input("Email:");
                if '@'not in email_usuario:
                    print("ERRO: Email inválido");
                else:
                    break;
            except ValueError:
                print("ERRO: Valor email inválido! Tente novamente")
            
        dados_usuario= {'id': id_usuario,'nome': nome_usuario,'idade': idade_usuario,'email': email_usuario}
        dados_usuario_lista.append(dados_usuario)
        print("Usuário cadastrado!\n\n")
        cadastrar_novamente = int(input("Deseja cadastrar outro usuário?\n\n1 - Novo usuário\n2 - Sair\n:"));
        if(cadastrar_novamente == 1):
                continue
        elif(cadastrar_novamente == 2):
                break;
        
           
            
def listar_usuarios():
    print("---USUÁRIOS CADASTRADOS---\n")
    for usuario in dados_usuario_lista:
            print("--" * 10);
            print(f"Nome: {usuario['nome']}\nIdade: {usuario['idade']}\nEmail: {usuario['email']}\n");
    
    while True:
        try:    
            opcoes_visualizar = int(input("Deseja sair?\n\n1 - Visualizar novamente\n2 - Sair\n:"));
            if(opcoes_visualizar == 1):
                listar_usuarios()
                break;
            elif(opcoes_visualizar == 2):
                break;
            else:
                print("Digito não corresponde as opções! Digite novamente.\n")
                
        except ValueError:
            print("ERRO: Valor incorreto! Digite Novamente\n")
            
    
def remover_usuario():
   print("---Remover usuário---\n")
   
   
   for usuario_remover in dados_usuario_lista:
        print(f"ID: {usuario_remover['id']}\nNome: {usuario_remover['nome']}\n");
   try:
        remover_id = int(input("Digite o ID do usuário que deseja remover: "));
        usuario_antes = len(dados_usuario_lista);
        
        for contador, usuarios_listas in enumerate(dados_usuario_lista):
            if usuarios_listas.get('id') == remover_id:
                dados_usuario_lista.pop(contador)
                break;        
        
        if len(dados_usuario_lista) < usuario_antes:    
            print(f"Usuário {remover_id} removido!!\n")
        else:
            print(f"ERRO: Usuário com ID {remover_id} não foi encontrado!")
            
        while True:
            try:
                opcoes_remover = int(input("\nDeseja sair?\n1 - Remover outro usuário\n2 - Sair\n:"))
                if(opcoes_remover == 1):
                    remover_usuario();
                    break;
                elif(opcoes_remover == 2):
                    break;
                else: 
                    print("ERRO: Valor não corresponde às opções! Digite novamente.");
            except ValueError:
                print("ERRO: Valor incorreto! Digite Novamente\n")
   except ValueError:
           print("ERRO: Digite um valor válido de ID\n")
       

sistema()