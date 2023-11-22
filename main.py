import yfinance as yf


def obter_dados(symbol):
    try:
        # Obter dados diretamente da API do Yahoo Finance
        stock = yf.Ticker(symbol)

        # Informações Gerais
        info = stock.info
        print(f"\nInformações para {symbol} ({info.get('shortName', 'N/A')})")
        print("-----------------------------------------------------")
        print(f"Setor: {info.get('sector', 'N/A')}")
        print(f"Indústria: {info.get('industry', 'N/A')}")
        print(f"País: {info.get('country', 'N/A')}")
        print(f"Exchange: {info.get('exchange', 'N/A')}")
        print(f"Moeda: {info.get('currency', 'N/A')}")

        # Estatísticas Principais
        stats = stock.history(period="1d").iloc[-1]
        print("\nEstatísticas Principais")
        print("------------------------")
        print(f"Preço Atual: {stats['Close']}")
        print(
            f"Variação Diária: {stats['Close'] - stats['Open']} ({((stats['Close'] - stats['Open']) / stats['Open']) * 100:.2f}%)")
        print(f"Volume Atual: {stats['Volume']}")

        # Informações Financeiras
        financials = stock.history(period="1y")
        print("\nInformações Financeiras (últimos 12 meses)")
        print("--------------------------------------------")
        print(financials)

    except Exception as e:
        print(f'Erro ao obter informações para {symbol}: {e}')


# Solicitar ao usuário um símbolo para pesquisa
symbol = input('Digite o símbolo que você deseja pesquisar (por exemplo, AAPL): ')
obter_dados(symbol)
