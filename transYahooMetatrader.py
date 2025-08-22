"""
Script para importar dados históricos de ativos financeiros do Yahoo Finance
(Formato: Date, Time, Open, High, Low, Close, Volume)
Objetivo: Exportar para CSV e utilizar no MetaTrader para backtests
"""

import yfinance as yf
import pandas as pd
import os

# === INPUTS DO USUÁRIO ===
ticker = input("Digite o código do papel (ex: VALE3.SA, PETR4.SA): ").strip()
periodo = "max"   # pode ser '1y', '5y', 'max', etc.
saida = r"g:\Meu Drive\Invest\ALGOTRADE\Inserção de dados\OUTPUT DATA COLLAB"

# === DOWNLOAD DOS DADOS ===
print(f"📥 Baixando dados de {ticker} do Yahoo Finance...")
df = yf.download(ticker, period=periodo)

# === ORGANIZAÇÃO DO DATAFRAME ===
df = df.reset_index()

# Garantir formato de data AAAA-MM-DD
df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')

# Inserir coluna "Time" com valor fixo (MetaTrader exige)
df.insert(1, 'Time', '00:00:00')

# Remover Adj Close, se existir
if 'Adj Close' in df.columns:
    df.drop(columns=['Adj Close'], inplace=True)

# Reordenar colunas no formato correto
df = df[['Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume']]

# === EXPORTAÇÃO ===
os.makedirs(saida, exist_ok=True)
arquivo_saida = os.path.join(saida, f"{ticker}.csv")

df.to_csv(arquivo_saida, index=False)
print(f"✅ Arquivo salvo em: {arquivo_saida}")

print("\nPré-visualização:")
print(df.head())

os.path()


