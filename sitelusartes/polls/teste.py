import sqlite3

conn = sqlite3.connect('')
cursor = conn.cursor()
nome_tabela = ''

#obtendo informações da tabela
cursor.execute ('PRAGMA table_info({})' .format(nome_tabela))

colunas -[tupla [1] for tupla in cursor.fetchall()]
print('Colunas:', colunas)

#listando as tabelas do banco de dados 
cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' ORDER BY name""")

print('tabelas;')
for tabela in cursor.fetchall():
    print("%s" % (tabela))

#obtendo o esquema da tabela
cursor.exeute("""SELECT sql FROM sqlite_master WHERE type='table' AND name=?""", (nome_tabela,))

print('Esquema:')
for esquema in cursor.fetchall():
    print("%s" % (esquema))


conn.close()