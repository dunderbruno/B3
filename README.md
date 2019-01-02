# B3

#### Conjunto de scripts para web scraping da cotação de ações de empresas listadas na B3.

### Preparação do banco de dados:

##### txttobd.py
   Lê um arquivo de texto com as empresas listadas e insere na tabela empresas.
   
##### gerartabelas.py
   Gera uma tabela para cada ítem da tabela 'empresas'.

### Scraping e download:

##### ibov.py
   Baixa índice Bovespa do dia.

##### preencher.py
   Consulta e salva os dados disponíveis das empresas listadas.
