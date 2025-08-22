# 📈 Yahoo Finance → MetaTrader

Este projeto tem como objetivo **importar dados históricos de ativos financeiros do Yahoo Finance** e convertê-los para o formato aceito pelo **MetaTrader**, permitindo realizar **backtests de estratégias** com facilidade.  

---

## 🎯 Objetivo
- Baixar cotações históricas (OHLCV: Data, Hora, Abertura, Máxima, Mínima, Fechamento e Volume).  
- Organizar os dados no formato exigido pelo MetaTrader (`Date, Time, Open, High, Low, Close, Volume`).  
- Exportar os dados para **CSV** e utilizá-los em backtests.  

---

## 🛠️ Tecnologias utilizadas
- **Python 3**  
- [yfinance](https://pypi.org/project/yfinance/) → para coletar dados do Yahoo Finance  
- **pandas** → para manipulação e organização dos dados  
- **os** → para gerenciamento de diretórios e exportação  

---

## 🚀 Como usar
1. Clone este repositório.  
2. Instale as dependências:
   ```bash
   pip install yfinance pandas
3. Execute o script:
   ```bash
  python yahoo_to_mt.py


5. Informe o ticker do ativo (ex: VALE3.SA, PETR4.SA).

6. O arquivo CSV será gerado na pasta de saída especificada no código.

## 📚 O que aprendi

- Como utilizar a biblioteca yfinance para coletar dados do Yahoo Finance.
- Manipulação de DataFrames no pandas (resetar índices, reordenar colunas, tratar datas).
- Como preparar dados em formato compatível com o MetaTrader.
- Boas práticas de exportação para CSV e organização de scripts em Python.

✨ Próximos passos

- Adicionar opção de escolher intervalos menores (1h, 15m, 1m) além de diário.
- Criar uma interface gráfica simples para facilitar o uso.
- Transformar o script em um executável para rodar sem precisar do Python instalado.
- Melhorar tratamento de erros (ex.: tickers inválidos ou falha na conexão).
