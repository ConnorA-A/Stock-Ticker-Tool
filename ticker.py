import yfinance as yf

while True:
    ticker = input("Enter a stock ticker (or 'quit' to exit): ")
    if ticker.lower() == 'quit':
        break
    try:
        stock = yf.Ticker(ticker)
        price = stock.info['currentPrice']
        print(f'The current price of {ticker.upper()} is ${price}')
    except KeyError:
       print("This ticker does not exist. Please try again.")