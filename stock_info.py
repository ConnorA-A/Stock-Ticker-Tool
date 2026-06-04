import yfinance as yf
while True:
    ticker = input("Enter the stock ticker symbol : ")
    if ticker.lower() == 'quit':
         break
    try:
        stock = yf.Ticker(ticker)
        DividendYield = stock.info.get('dividendYield', '0.00')
        PricetoBook = stock.info.get('priceToBook', 'N/A')
        averageAnalystRating = stock.info.get('averageAnalystRating', 'N/A')
        fiftyDayAverageChangePercent = stock.info.get('fiftyDayAverageChangePercent', 0)
        forwardPE = stock.info.get('forwardPE', 'N/A')
        marketCap = stock.info.get('marketCap', 0)
        forwardEPS = stock.info.get('forwardEps', 'N/A')
        sector = stock.info.get('sector', 'N/A')
        industry = stock.info.get('industry', 'N/A')
        beta = stock.info.get('beta', 'N/A')

        if PricetoBook != 'N/A':
            PricetoBook = round(PricetoBook, 2)


        if marketCap >= 1e12:
            marketCap_str = f"{round(marketCap / 1e12, 1)}T"
        elif marketCap >= 1e9:
            marketCap_str = f"{round(marketCap / 1e9, 1)}B"
        elif marketCap >= 1e6:
            marketCap_str = f"{round(marketCap / 1e6, 1)}m"
        else:
            marketCap_str = f"{marketCap}"


        if forwardPE != 'N/A':
            forwardPE = round(forwardPE, 2)
        
        if forwardEPS != 'N/A':
            forwardEPS = round(forwardEPS, 2)

        if beta != 'N/A':
            beta = round(beta, 2)   

        print(f"Dividend Yield: {DividendYield}%")
        print(f"Price to Book: {PricetoBook}")
        print(f"Average Analyst Rating: {averageAnalystRating}")
        print(f"50 Day Average Change Percent: {round(fiftyDayAverageChangePercent * 100, 1)}%")
        print(f"Forward PE: {forwardPE}")
        print(f"Market Cap: {marketCap_str}")
        print(f"Forward EPS: {forwardEPS}")
        print(f"Sector: {sector}")
        print(f"Industry: {industry}")
        print(f"Beta: {beta}")

    except KeyError:
        print("This ticker does not exist. Please try again")
    except ValueError:
        print("Please enter a valid ticker")

