"""Preenche a tabela."""
import sqlite3
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import date
import time
import os

inicio = time.time()

hoje = str(date.today())

conn = sqlite3.connect('b3.db')
cursor = conn.cursor()

codigos = cursor.execute("""SELECT code FROM empresas""")

urlbase = 'http://cotacoes.economia.uol.com.br/acao/index.html?codigo='

baixados = 0
for i in codigos.fetchall():
    print('entrei')
    os.system('clear')
    baixados += 1
    print('Baixados %d / 1974.' % baixados)
    html = urlopen(urlbase+i[0])
    bsObj = BeautifulSoup(html.read(), 'html5lib')
    body = bsObj.findAll("td")
    dados = [i.getText() for i in body]
    if len(dados) > 1:
        del(dados[0])
        dados = [hoje] + dados
        # print(dados)
        command = 'INSERT INTO %s (data, var, var_percentual, ultima, maxima, minima, abertura, volume) VALUES (?, ?, ?, ?, ?, ?, ?, ?)' % i[0][:-3]
        cursor.execute("""%s""" % command, dados)

urlibov = 'http://cotacoes.economia.uol.com.br/bolsas/index.html?indice=.BVSP'

html = urlopen(urlibov)
bsObj = BeautifulSoup(html.read(), 'html5lib')
body = bsObj.findAll("td")
dados = [i.getText() for i in body]
if len(dados) > 1:
    del(dados[0])
    dados = [hoje] + dados
    print(dados)
    command = 'INSERT INTO ibovespa (data, var, var_percentual, ultima, maxima, minima, abertura, volume) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
    cursor.execute("""%s""" % command, dados)


conn.commit()
conn.close()
fim = time.time()

print((fim-inicio)/60)
