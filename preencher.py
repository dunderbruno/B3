"""Preenche a tabela."""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sqlite3
from datetime import date

today = date.today()

conn = sqlite3.connect('b3.db')
cursor = conn.cursor()

codigos = cursor.execute("""SELECT code
                  FROM empresas""")

# print(codigos.fetchall())

urlbase = 'http://cotacoes.economia.uol.com.br/acao/index.html?codigo='
for i in codigos.fetchall():
    print(i[0])
    html = urlopen(urlbase+i[0])
    bsObj = BeautifulSoup(html.read(), 'html5lib')
    body = bsObj.findAll("td")
    dados = [i.getText() for i in body]
    if len(dados) > 1:
        del(dados[0])
        print(dados)
        command = 'INSERT INTO %s (var, var_percentual, ultima, maxima, minima, abertura, volume) VALUES (?, ?, ?, ?, ?, ?, ?)' % i[0][:-3]
        cursor.execute("""%s""" % command, dados)


conn.commit()
conn.close()
