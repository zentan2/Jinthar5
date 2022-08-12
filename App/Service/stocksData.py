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
    tickers = yf.Tickers(" ".join(stocksPortfolio[number]))

    for stockTicker, stockInfo in tickers.tickers.items():
        temp = {
            "symbol":stockInfo.info['symbol'],
            "name":stockInfo.info['shortName'],
            "currentPrice":stockInfo.info['regularMarketPrice'],
            "dayHigh":stockInfo.info['dayHigh'],
            "dayLow":stockInfo.info['dayLow'],
        }
        portfolio.append(temp)
        
    return json.dumps(portfolio)


# testing code
if __name__ == "__main__":
    # print(stockInfo("aapl"))
    # print(stockInfo("12345"))
    # print(portfolioInfo(2))   
    print(portfolioInfo(1))     
