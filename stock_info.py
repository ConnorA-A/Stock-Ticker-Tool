import yfinance as yf
while True:
    ticker = input("Enter the stock ticker symbol : ")
    if ticker.lower() == 'quit':
         break
    try:
        stock = yf.Ticker(ticker)
        DividendYield = stock.info['dividendYield']
        PricetoBook = stock.info['priceToBook']
        averageAnalystRating = stock.info['averageAnalystRating']
        fiftyDayAverageChangePercent = stock.info['fiftyDayAverageChangePercent']
        forwardPE = stock.info['forwardPE']
        marketCap = stock.info['marketCap']
        forwardEPS = stock.info['forwardEps']
        sector = stock.info['sector']
        industry = stock.info['industry']
        beta = stock.info['beta']
        print(f"Dividend Yield: {DividendYield}")
        print(f"Price to Book: {PricetoBook}")
        print(f"Average Analyst Rating: {averageAnalystRating}")
        print(f"50 Day Average Change Percent: {fiftyDayAverageChangePercent}")
        print(f"Forward PE: {forwardPE}")
        print(f"Market Cap: {round(marketCap,1)}T")
        print(f"Forward EPS: {forwardEPS}")
        print(f"Sector: {sector}")
        print(f"Industry: {industry}")
        print(f"Beta: {beta}")

    except KeyError:
        print("This ticker does not exist. Please try again")

