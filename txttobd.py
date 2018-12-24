u"""Lê arquivo e grava no banco de dados."""

import sqlite3

conn = sqlite3.connect('b3.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE empresas (name, code)""")

with open('codigos.txt', 'r') as codigos:
    lista = codigos.readlines()

for i in range(0, len(lista), 2):
    command = 'INSERT INTO empresas (name, code) VALUES (?, ?)'
    cursor.execute("""%s""" % command, (lista[i][:-1], lista[i+1][:-1]))

conn.commit()
conn.close()
