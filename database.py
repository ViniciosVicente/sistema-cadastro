import sqlite3

# 1. Conectar ao banco de dados (cria se não existir)
conn = sqlite3.connect('exemplo.db')

# 2. Criar um objeto cursor para interagir
cursor = conn.cursor()

# 3. Criar uma tabela (exemplo)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER
    )
''')

# 4. Inserir dados
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Ana', 28)")
conn.commit() # Salvar alterações

# 5. Consultar dados
cursor.execute("SELECT * FROM usuarios")
print(cursor.fetchall())

# 6. Fechar conexão
conn.close()
