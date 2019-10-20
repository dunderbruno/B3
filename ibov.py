"""Preenche a tabela."""
import sqlite3
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import date
import time
import os
import ssl

hoje = str(date.today())

conn = sqlite3.connect('b3.db')
cursor = conn.cursor()

urlibov = 'http://cotacoes.economia.uol.com.br/bolsas/index.html?indice=.BVSP'

context = ssl._create_unverified_context()
html = urlopen(urlibov, context=context)
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
