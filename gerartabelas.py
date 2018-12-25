"""Gerar tabelas no banco de dados."""

import sqlite3
import time

inicio = time.time()

conn = sqlite3.connect('b3.db')
cursor = conn.cursor()

nomes = cursor.execute("""SELECT code FROM empresas""")
for i in nomes.fetchall():
    command = 'CREATE TABLE %s (id PRIMARYKEY, data TEXT, resultado INTEGER, var REAL, var_percentual REAL, ultima REAL, maxima REAL, minima REAL, abertura REAL, volume INTEGER)' % i[0][:-3]
    cursor.execute("""%s""" % command)
    print(i[0])

conn.commit()
conn.close()

fim = time.time()

print((fim-inicio)/60)
