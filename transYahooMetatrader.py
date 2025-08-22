# CÓDIGO FEITO PARA IMPORTAR DADOS DE PREÇOS HISTÓRICOS DE ATIVOS FINANCEIROS
# (DATA, HORA, ABERTURA, MÁXIMA, MÍNIMA, FECHAMENTO E VOLUME NEGOCIADO) DO
# YAHOO FINANCE DIRETO PARA O METATRADER FIZ ISSO PARA REALIZAR BACKTESTS

#from google.colab import drive
#drive.mount('/content/drive')
# A ORDEM DOS DADOS DEVE SER A SEGUINTE ---> Date, Time, Open, High, Low, Close, Volume


import pdb
import yfinance as yf
import pandas as pd

# Definindo o ticker e o período desejado (VER O NOME NO YAHOO)
# O CÓDIGO DO PAPEL PODE SER ENCONTRADO NO https://finance.yahoo.com/
# POR EXEMPLO VALE3 DEVE-SE ESCREVER VALE3.SA
ticker = input("Digite o código do papel (max period): ")
periodo = "max"

# Baixando os dados históricos e armazenando em um DataFrame
df = yf.download(ticker, period=periodo)

# COMO JÁ OCORREU ERROS DE FORMATO PRECISO EXCLUIR OS CARACTERES EXCEDENTES DA
# COLUNA TIME

# TRANSFORMO O INDICE "DATA" PARA COLUNA PARA FACILITAR A MANIPULAÇÃO
df = df.reset_index()

# REMOVER OS VALORES ALÉM DO DÉCIMO CARACTERE NA COLNA 'Date'
df['Date'] = df['Date'].astype(str).str[:10]

# Preciso ADICIONAR uma coluna entre a primeira coluna e a segunda coluna, que tenha a seguinte informação (00:00:00)
df.insert(1, 'Time', '00:00:00')

# CASO VENHA A COLUNA ADJ CLOSE (eu prefiro nao usar)
if 'Adj Close' in df.columns:
    df = df.drop(columns=['Adj Close'])
    print("Coluna 'Adj Close' deletada.")
else:
    print("Coluna 'Adj Close' não encontrada no DataFrame.")


# Colocar na ordem OHLC
df = df[['Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume']]

df.head()


#EXPORTAÇÃO PARA CSV
#from google.colab import drive
#drive.mount('/content/drive')

#PARA PEGAR O DIRETÓRIO UTILIZADO
import os
print(os.getcwd())


#df.to_csv(f'/content/drive/My Drive/Invest/ALGOTRADE/Inserção de dados/OUTPUT DATA COLLAB/{ticker}.csv', index=False)
df.to_csv(f'g:\Meu Drive\Invest\ALGOTRADE\Inserção de dados\OUTPUT DATA COLLAB\{ticker}.csv', index=False)


# dfAdj.to_csv('/content/drive/My Drive/Invest/ALGOTRADE/Inserção de dados/OUTPUT DATA COLLAB/.csv', index=False)

df