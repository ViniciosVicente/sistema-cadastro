
dados_usuario = {};
dados_usuario_lista = [];
def sistema():
    
    while True:
        print("\n--Sistema de Cadastramento--\n");
        try:
            opcoes = int(input("Opções:\n1 - Cadastrar usuário\n2 - Usuários cadastrados\n3 - Remove usuário cadastrado\n4 - Sair\n:"));
            if(opcoes == 1):
                cadastrarUsuario();
            elif(opcoes == 2):
                usuarioCadastrados();
            elif(opcoes == 3): 
                removerUsuario();
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
def cadastrarUsuario():
    
    print("--- CADASTRO USUÁRIO ---\n")
    while True:
        id_usuario = gerar_novo_id()
    
        try:
            nome_usuario = input("\nNome:");
            idade_usuario = int(input("Idade:"));
            email_usuario = input("Email:");
            dados_usuario= {'id': id_usuario,'nome': nome_usuario,'idade': idade_usuario,'email': email_usuario}
            dados_usuario_lista.append(dados_usuario)
            print("Usuário cadastrado!\n\n")
            cadastrar_novamente = int(input("Deseja cadastrar outro usuário?\n\n1 - Novo usuário\n2 - Sair\n:"));
            if(cadastrar_novamente == 1):
                continue
            elif(cadastrar_novamente == 2):
                print(dados_usuario_lista)
                break;
        except ValueError:
            print("ERRO: Valor inválido! Tente novamente")
           
            
def usuarioCadastrados():
    print("---USUÁRIOS CADASTRADOS---\n")
    for usuario in dados_usuario_lista:
            print("--" * 10);
            print(f"Nome: {usuario['nome']}\nIdade: {usuario['idade']}\nEmail: {usuario['email']}\n");
    
    while True:
        try:    
            opcoes_visualizar = int(input("Deseja sair?\n\n1 - Visualizar novamente\n2 - Sair\n:"));
            if(opcoes_visualizar == 1):
                usuarioCadastrados()
                break;
            elif(opcoes_visualizar == 2):
                break;
            else:
                print("Digito não corresponde as opções! Digite novamente.\n")
                
        except ValueError:
            print("ERRO: Valor incorreto! Digite Novamente\n")
            
    
def removerUsuario():
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
                    removerUsuario();
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