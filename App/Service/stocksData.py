import yfinance as yf
import json

def stockInfo(stock):
    
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


# testing code
if __name__ == "__main__":
    print(stockInfo("aapl"))
    print(stockInfo("12345"))
