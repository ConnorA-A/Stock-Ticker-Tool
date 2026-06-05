import yfinance as yf
import pandas as pd
while True:
    ticker = input("Enter the stock ticker/s symbol (if two tickers, seperate with a comma) : ")
    tickers = ticker.split(",")
    if ticker.lower() == 'quit':
         break
    if len(tickers) == 1:
        ticker = tickers[0].strip()
        try:
            stock = yf.Ticker(ticker)
            current_price = stock.info['currentPrice']
            daily_change = stock.info['regularMarketChangePercent']
            fifty_two_week_high = stock.info['fiftyTwoWeekHigh']
            fifty_two_week_low = stock.info['fiftyTwoWeekLow']
            distance_from_fifty_two_week_high = (((current_price - fifty_two_week_high) / fifty_two_week_high) * 100)
            if distance_from_fifty_two_week_high > 0:
                distance_from_fifty_two_week_high = f"{round(distance_from_fifty_two_week_high, 2)}% above 52 week high"
            else:
                distance_from_fifty_two_week_high = f"{abs(round(distance_from_fifty_two_week_high, 2))}% below 52 week high"
            distance_from_fifty_two_week_low = (((current_price - fifty_two_week_low) / fifty_two_week_low) * 100)
            if distance_from_fifty_two_week_low > 0:
                distance_from_fifty_two_week_low = f"{round(distance_from_fifty_two_week_low, 2)}% above 52 week low"
            else:
                distance_from_fifty_two_week_low = f"{abs(round(distance_from_fifty_two_week_low, 2))}% below 52 week low"
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

            print()
            print(f"Current Price: ${round(current_price, 2)}")
            print(f"Daily Change: {round(daily_change, 2)}%")
            print(f"52 Week High: ${round(fifty_two_week_high, 2)}")
            print(f"52 Week Low: ${round(fifty_two_week_low, 2)}")
            print(f"Current price is trading at {distance_from_fifty_two_week_high} and {distance_from_fifty_two_week_low}")

            print()
            print(f"Dividend Yield: {DividendYield}%")
            print(f"Price to Book: {PricetoBook}")
            print(f"Average Analyst Rating: {averageAnalystRating}")
            print(f"50 Day Average Percent Change: {round(fiftyDayAverageChangePercent * 100, 1)}%")
            print(f"Forward PE: {forwardPE}")
            print(f"Market Cap: {marketCap_str}")
            print(f"Forward EPS: {forwardEPS}")
            print(f"Sector: {sector}")
            print(f"Industry: {industry}")
            print(f"Beta: {beta}")



            print("\n--- 6 Month Price History ---")
            hist = stock.history(period="6mo")
            average_close = hist['Close'].mean()
            high = hist['Close'].max()
            low = hist['Close'].min()
            average_daily_return = hist['Close'].pct_change().mean() * 100
            best_day = hist['Close'].pct_change().max() * 100
            best_day_date = hist['Close'].pct_change().idxmax()
            worst_day = hist['Close'].pct_change().min() * 100
            worst_day_date = hist['Close'].pct_change().idxmin()
            print(f"Average Close Price: ${average_close:.2f}")
            print(f"Highest Closing Price: ${high:.2f}")
            print(f"Lowest Closing Price: ${low:.2f}")
            print(f"Average Daily Return: {average_daily_return:.2f}%")
            print(f"Best Day: {best_day_date.strftime('%d/%m/%Y')} with a return of {best_day:.2f}%")
            print(f"Worst Day: {worst_day_date.strftime('%d/%m/%Y')} with a return of {worst_day:.2f}%")
            print()

        except KeyError:
            print("This ticker does not exist. Please try again")
        except ValueError:
            print("Please enter a valid ticker")      
    elif len(tickers) == 2:
        ticker = tickers[0].strip()
        comparison_ticker = tickers[1].strip()
        try:
            stock = yf.Ticker(ticker)
            comparison_stock = yf.Ticker(comparison_ticker)
            
            price = stock.info['currentPrice']
            comparison_price = comparison_stock.info['currentPrice']
            
            daily_change = stock.info['regularMarketChangePercent']
            comparison_daily_change = comparison_stock.info['regularMarketChangePercent']

            fifty_two_week_high = stock.info['fiftyTwoWeekHigh']
            comparison_fifty_two_week_high = comparison_stock.info['fiftyTwoWeekHigh']

            fifty_two_week_low = stock.info['fiftyTwoWeekLow']
            comparison_fifty_two_week_low = comparison_stock.info['fiftyTwoWeekLow']

            percent_from_fifty_two_week_high = ((price - fifty_two_week_high) / fifty_two_week_high) *100
            comparison_percent_from_fifty_two_week_high = ((comparison_price - comparison_fifty_two_week_high) / comparison_fifty_two_week_high) *100

            percent_from_fifty_two_week_low = ((price - fifty_two_week_low) / fifty_two_week_low) *100
            comparison_percent_from_fifty_two_week_low = ((comparison_price - comparison_fifty_two_week_low) / comparison_fifty_two_week_low) *100

            dividend_yield = stock.info.get('dividendYield', 0.00)
            comparison_dividend_yield = comparison_stock.info.get('dividendYield', 0.00)

            price_to_book = stock.info.get('priceToBook', 'N/A')
            if price_to_book != 'N/A':
                price_to_book = price_to_book
            comparison_price_to_book = comparison_stock.info.get('priceToBook', 'N/A')
            if comparison_price_to_book != 'N/A':
                comparison_price_to_book = comparison_price_to_book
            
            average_analyst_rating = stock.info.get('averageAnalystRating', 'N/A')
            comparison_average_analyst_rating = comparison_stock.info.get('averageAnalystRating', 'N/A')

            fifty_day_average_change_percent = stock.info.get('fiftyDayAverageChangePercent', 0)
            comparison_fifty_day_average_change_percent = comparison_stock.info.get('fiftyDayAverageChangePercent', 0)

            forwardPE = stock.info.get('forwardPE', 'N/A')
            if forwardPE != 'N/A':
                forwardPE = forwardPE
            comparison_forwardPE = comparison_stock.info.get('forwardPE', 'N/A')
            if comparison_forwardPE != 'N/A':
                comparison_forwardPE = comparison_forwardPE

            marketcap = stock.info.get('marketCap', 0)
            if marketcap >= 1e12:
                marketcap_str = f"{round(marketcap / 1e12, 1)}T"
            elif marketcap >= 1e9:
                marketcap_str = f"{round(marketcap / 1e9, 1)}B"
            elif marketcap >= 1e6:
                marketcap_str = f"{round(marketcap / 1e6, 1)}m"
            else:
                marketcap_str = f"{marketcap}"

            comparison_marketcap = comparison_stock.info.get('marketCap', 0)
            if comparison_marketcap >= 1e12:
                comparison_marketcap_str = f"{round(comparison_marketcap / 1e12, 1)}T"
            elif comparison_marketcap >= 1e9:
                comparison_marketcap_str = f"{round(comparison_marketcap / 1e9, 1)}B"
            elif comparison_marketcap >= 1e6:
                comparison_marketcap_str = f"{round(comparison_marketcap / 1e6, 1)}m"
            else:
                comparison_marketcap_str = f"{comparison_marketcap}"

            forwardEPS = stock.info.get('forwardEps', 'N/A')
            if forwardEPS != 'N/A':
                forwardEPS = forwardEPS
            comparison_forwardEPS = comparison_stock.info.get('forwardEps', 'N/A')
            if comparison_forwardEPS != 'N/A':
                comparison_forwardEPS = comparison_forwardEPS

            sector = stock.info.get('sector', 'N/A')
            comparison_sector = comparison_stock.info.get('sector', 'N/A')

            industry = stock.info.get('industry', 'N/A')
            comparison_industry = comparison_stock.info.get('industry', 'N/A')

            beta = stock.info.get('beta', 'N/A')
            if beta != 'N/A':
                beta = round(beta, 2) 
            comparison_beta = comparison_stock.info.get('beta', 'N/A')
            if comparison_beta != 'N/A':
                comparison_beta = round(comparison_beta, 2)
                                  


            
            

            





            data = {
                ticker.upper(): [f"${round(price, 2)}", 
                                 f"{round(daily_change, 2)}%", 
                                 f"${round(fifty_two_week_high, 2)}", 
                                 f"${round(fifty_two_week_low, 2)}", 
                                 f"{round(percent_from_fifty_two_week_high, 2)}%", 
                                 f"{round(percent_from_fifty_two_week_low, 2)}%", 
                                 "",
                                 f"{round(dividend_yield, 2)}%",
                                 f"{round(price_to_book, 2)}",
                                 f"{average_analyst_rating}",
                                 f"{round(fifty_day_average_change_percent * 100, 2)}%",
                                 f"{round(forwardPE, 2)}",
                                 f"{marketcap_str}",
                                 f"{round(forwardEPS, 2)}",
                                 f"{sector}",
                                 f"{industry}",
                                 f"{round(beta, 2)}"],
                                 

                                 
                comparison_ticker.upper(): [f"${round(comparison_price, 2)}", 
                                            f"{round(comparison_daily_change, 2)}%", 
                                            f"${round(comparison_fifty_two_week_high, 2)}", 
                                            f"${round(comparison_fifty_two_week_low, 2)}", 
                                            f"{round(comparison_percent_from_fifty_two_week_high, 2)}%", 
                                            f"{round(comparison_percent_from_fifty_two_week_low, 2)}%", 
                                            "",
                                            f"{round(comparison_dividend_yield, 2)}%",
                                            f"{round(comparison_price_to_book, 2)}",
                                            f"{comparison_average_analyst_rating}",
                                            f"{round(comparison_fifty_day_average_change_percent * 100, 2)}%",
                                            f"{round(comparison_forwardPE, 2)}",
                                            f"{comparison_marketcap_str}",
                                            f"{round(comparison_forwardEPS, 2)}",
                                            f"{comparison_sector}",
                                            f"{comparison_industry}",
                                            f"{round(comparison_beta, 2)}"],
            }
            df = pd.DataFrame(data, index = [
                'Current Price', 
                'Daily Change', 
                '52 Week High', 
                '52 Week Low', 
                'Percent from 52 Week High', 
                'Percent from 52 Week Low',
                  "", 
                  "Dividend Yield", 
                  "Price to Book",
                  "Average Analyst Rating",
                  "50 Day Average Percent Change",
                  "ForwardPE",
                  "Marketcap",
                  "ForwardEPS",
                  "Sector",
                  "Industry",
                  "Beta"])
           
           
            print(df)

            print("\n--- 6 Month Price History ---")

            hist = stock.history(period="6mo")
            comparison_hist = comparison_stock.history(period="6mo")

            average_close = hist['Close'].mean()
            comparison_average_close = comparison_hist['Close'].mean()

            high = hist['Close'].max()
            comparison_high = comparison_hist['Close'].max()

            low = hist['Close'].min()
            comparison_low = comparison_hist['Close'].min()

            average_daily_return = hist['Close'].pct_change().mean() * 100
            comparison_average_daily_return = comparison_hist['Close'].pct_change().mean() * 100

            best_day = hist['Close'].pct_change().max() * 100
            best_day_date = hist['Close'].pct_change().idxmax()
            comparison_best_day = comparison_hist['Close'].pct_change().max() * 100
            comparison_best_day_date = comparison_hist['Close'].pct_change().idxmax()
            
   


            data = {
                ticker.upper(): [f"${round(average_close, 2)}",
                                 f"${round(high, 2)}",
                                 f"${round(low, 2)}",
                                 f"{round(average_daily_return, 2)}%",
                                 f"{best_day_date.strftime('%d/%m/%Y')}: {round(best_day, 2)}%"],
                                



                comparison_ticker.upper(): [f"${round(comparison_average_close, 2)}",
                                            f"${round(comparison_high, 2)}",
                                            f"${round(comparison_low, 2)}",
                                            f"{round(comparison_average_daily_return, 2)}%",
                                            f"{comparison_best_day_date.strftime('%d/%m/%Y')}: {round(comparison_best_day, 2)}%"]
            }
            df = pd.DataFrame(data, index = [
                'Average Close Price',
                'Highest Closing Price',
                'Lowest Closing Price',
                'Average Daily Return',
                'Best Day (Date : Return)'
            ])
            print(df.to_string(col_space=20))





        except KeyError:
            print("One or both of the tickers do not exist. Please try again")
        except ValueError:
            print("Please enter valid tickers")
    else:
        print("Please enter only one or two tickers")
        continue

    
    