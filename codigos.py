u"""Scraping de nomes e códigos de empresas listadas na B3."""

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://cotacoes.economia.uol.com.br/acoes-bovespa.html?exchangeCode=.BVSP&page=1&size=2000'
html = urlopen(url)
bsObj = BeautifulSoup(html.read(), 'html5lib')
codes = bsObj.findAll("span")
with open('codigos.txt', 'w') as lista:
    for i in codes:
        lista.write(i.getText()+'\n')
