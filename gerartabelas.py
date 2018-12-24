"""Gerar tabelas no banco de dados."""

import sqlite3


conn = sqlite3.connect('b3.db')
cursor = conn.cursor()

nomes = cursor.execute("""SELECT code FROM empresas""")
for i in nomes.fetchall():
    command = 'CREATE TABLE %s (flag INTEGER, var REAL, var_percentual REAL, ultima REAL, maxima REAL, minima REAL, abertura REAL, volume INTEGER)' % i[0][:-3]
    # print(command)
    cursor.execute("""%s""" % command)
    print(i[0])
# cursor.execute("""CREATE TABLE ships (race text, alive real)""")

conn.commit()
conn.close()
