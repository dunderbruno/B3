"""Preenche a tabela."""
import sqlite3
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import date
import time

inicio = time.time()
today = date.today()

conn = sqlite3.connect('b3.db')
cursor = conn.cursor()

codigos = cursor.execute("""SELECT code FROM empresas""")

urlbase = 'http://cotacoes.economia.uol.com.br/acao/index.html?codigo='
hoje = str(date.today())
for i in codigos.fetchall():
    print(i[0])
    html = urlopen(urlbase+i[0])
    bsObj = BeautifulSoup(html.read(), 'html5lib')
    body = bsObj.findAll("td")
    dados = [i.getText() for i in body]
    if len(dados) > 1:
        del(dados[0])
        dados = [hoje] + dados
        print(dados)
        command = 'INSERT INTO %s (data, var, var_percentual, ultima, maxima, minima, abertura, volume) VALUES (?, ?, ?, ?, ?, ?, ?, ?)' % i[0][:-3]
        cursor.execute("""%s""" % command, dados)


conn.commit()
conn.close()
fim = time.time()

print((fim-inicio)/60)
