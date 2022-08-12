import yfinance as yf
import json

# sample data for testing
portfolio = [
    ['appl', 'spy', 'amd'],
    ['baba', 'amc', 'tsla'],
    ['crm', 'mrna', 'meta', 'iau'],
    ['msft']]

def stockInfo(stock):
    #obtains information of a single stock
    stockData = yf.Ticker(stock)
    if stockData.info['regularMarketPrice'] == None:
        return "Invalid Stock ticker"
    else:
        stockDictionary = {
            "symbol":stockData.info['symbol'],
            "name":stockData.info['shortName'],
            "currentPrice":stockData.info['regularMarketPrice'],
            "dayHigh":stockData.info['dayHigh'],
            "dayLow":stockData.info['dayLow'],
        }
        return json.dumps(stockDictionary)

def portfolioInfo(number, stocksPortfolio=portfolio):
    # obtains stock information for all the stocks in the list
    ###  change to retrieve data from sql!
    portfolio = []
    for stocks in stocksPortfolio[number]:
        portfolio.append(stockInfo(stocks))
    return portfolio


# testing code
if __name__ == "__main__":
    # print(stockInfo("aapl"))
    # print(stockInfo("12345"))
    print(portfolioInfo(3))     
