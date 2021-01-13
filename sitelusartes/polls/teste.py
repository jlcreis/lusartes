import sqlite3

conn = sqlite3.connect('django.db') #my database
cursor = conn.cursor()
nome_tabela = 'Produtos' #nome da tabekla

#obtendo informações da tabela
cursor.execute ('PRAGMA table_info({})' .format(nome_produto))



#listando as tabelas do banco de dados 
cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' ORDER BY name""")

print('tabelas;')
for tabela in cursor.fetchall():
    print("%s" % (tabela))

#obtendo o esquema da tabela
cursor.exeute("""SELECT sql FROM sqlite_master WHERE type='table' AND name=?""", (Produtos))

print('Esquema:')
for esquema in cursor.fetchall():
    print("%s" % (esquema))


conn.close()