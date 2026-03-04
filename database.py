import sqlite3

conn = sqlite3.connect('banco_cadastro.db')

# 2. Criar um objeto cursor para interagir
cursor = conn.cursor()


create_table_query = '''
    CREATE TABLE Usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    idade INTEGER,
    email TEXT
);
'''

cursor.execute()
conn.commit() 
cursor.execute("SELECT * FROM usuarios")
print(cursor.fetchall())

conn.close()
