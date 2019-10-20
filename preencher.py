"""
Preenche a tabela.

Consulta os dados e salva nas respectivas tabelas.
"""

import os
import sqlite3
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import date, datetime
from threading import Thread
import requests
import json

conn = sqlite3.connect('b3.db', check_same_thread=False)
cursor = conn.cursor()
codigos = cursor.execute("""SELECT code FROM empresas""").fetchall()
conn.close()
# url = 'http://cotacoes.economia.uol.com.br/acao/index.html?codigo='
url = 'https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/{}'
iteracoes = 0


def getDailyQuotation(stock_id):
    url = "https://api.cotacoes.uol.com/asset/intraday/list/"
    querystring = {"format":"JSON","fields":"price,high,low,open,volume,close,bid,ask,change,pctChange,date","item":stock_id,"\n":"","":"","%0A":""}
    response = requests.request("GET", url, headers={}, params=querystring).json()
    try:
        stock_data = response.get('docs')[0]
        stock_data['date'] = format_date(stock_data['date'])
        return stock_data
    except Exception as e:
        return None

def format_date(date_string):
    return datetime.strftime(datetime.strptime(date_string,"%Y%m%d%H%M%S"), "%Y-%m-%dT%H:%M:%SZ")

def getvalues(start):
    for i in range(start, int(len(codigos)), 4):
        os.system('clear')
        global iteracoes
        iteracoes += 1
        print('Baixados %d / 1974.' % iteracoes)
        html = urlopen(url.format(codigos[i][0].replace('.', '-').lower()))
        bsObj = BeautifulSoup(html.read(), 'html5lib')

        stock_name =  codigos[i][0][:-3]
        stock_id = bsObj.find("div", {'class':'financial-market-full stockAcao stockPage'})['data-id']
        data = getDailyQuotation(stock_id)

        #Only save on table if there is data
        if data:
            save_values_on_db(data, stock_name)
        else:
            continue

def save_values_on_db(data, table_name):
    conn = sqlite3.connect('b3.db', check_same_thread=False)
    cursor = conn.cursor()
    command = "INSERT INTO {} (data, var, var_percentual, ultima, maxima, minima, abertura, volume) VALUES ('{}', {}, {}, {}, {}, {}, {}, {})".format(
        table_name,
        data.get('date'),
        data.get('change'),
        data.get('pctChange'),
        data.get('close'),
        data.get('high'),
        data.get('low'),
        data.get('open'),
        data.get('volume')
    )

    cursor.execute(command)
    conn.commit()
    conn.close()


a = Thread(target=getvalues, args=(0,))
b = Thread(target=getvalues, args=(1,))
c = Thread(target=getvalues, args=(2,))
d = Thread(target=getvalues, args=(3,))

a.start()
b.start()
c.start()
d.start()
