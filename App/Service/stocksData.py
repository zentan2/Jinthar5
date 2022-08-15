import yfinance as yf
from flask import jsonify
import json
import pandas as pd

# sample data for testing
portfolio = [
    ['appl', 'spy', 'amd'],
    ['baba', 'amc', 'tsla'],
    ['OV8.SI', 'G3B.SI', 'D05.SI', 'U11.SI'],
    ['msft']]

stocks = [
    {"PortfolioId":1,"Ticker":"OV8.SI","Quantity":10000,"Price":1.65,"Name":"Sheng Siong","MarketValue":1.62,"UnrealisedPnL":-300.0,"UnrealisedPnLPercentage":-1.82},
    {"PortfolioId":1,"Ticker":"G3B.SI","Quantity":20000,"Price":3.31,"Name":"Nikko AM STI ETF","MarketValue":3.34,"UnrealisedPnL":600.0,"UnrealisedPnLPercentage":0.91},
    {"PortfolioId":1,"Ticker":"D05.SI","Quantity":8000,"Price":31.97,"Name":"DBS","MarketValue":32.94,"UnrealisedPnL":7760.0,"UnrealisedPnLPercentage":3.03},
    {"PortfolioId":1,"Ticker":"U11.SI","Quantity":16000,"Price":25.3,"Name":"UOB","MarketValue":27.3,"UnrealisedPnL":32000.0,"UnrealisedPnLPercentage":7.91},
    {"PortfolioId":2,"Ticker":"nvda","Quantity":100,"Price":177.22,"Name":"NVIDIA Corporation","MarketValue":187.09,"UnrealisedPnL":987.0,"UnrealisedPnLPercentage":5.57},
    {"PortfolioId":2,"Ticker":"meta","Quantity":20,"Price":170.5,"Name":"Meta Platforms, Inc.","MarketValue":180.5,"UnrealisedPnL":200.0,"UnrealisedPnLPercentage":5.87},
    {"PortfolioId":2,"Ticker":"intc","Quantity":50,"Price":38.22,"Name":"Intel Corporation","MarketValue":36.11,"UnrealisedPnL":-105.5,"UnrealisedPnLPercentage":-5.52},
    {"PortfolioId":2,"Ticker":"spy","Quantity":10,"Price":410.22,"Name":"SPDR S&P 500","MarketValue":427.1,"UnrealisedPnL":168.8,"UnrealisedPnLPercentage":4.11},
    {"PortfolioId":2,"Ticker":"aapl","Quantity":20,"Price":120.5,"Name":"Apple Inc.","MarketValue":172.1,"UnrealisedPnL":1032.0,"UnrealisedPnLPercentage":42.82}
    ]


all_df = pd.DataFrame(stocks)


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

def populatePortfolioInfo(portfolios):
    # obtains stock information for all the stocks in the list
    ###  change to retrieve data from sql!
    portfolio = {}
    tickers = yf.Tickers(" ".join(portfolios))

    for stockTicker, stockInfo in tickers.tickers.items():
        portfolio[stockTicker] = {
            "name":stockInfo.info['shortName'],
            "currentPrice":stockInfo.info['regularMarketPrice']
        }  
    return portfolio

def retrieveStockUpdates(df):
    tickers = list(set(df['Ticker']))
    updatedPortfolioInfo = populatePortfolioInfo(tickers)
    df['Name'] = df["Ticker"].apply(lambda x : updatedPortfolioInfo[x.upper()]["name"])
    df['MarketValue'] = df["Ticker"].apply(lambda x : updatedPortfolioInfo[x.upper()]["currentPrice"])
    df['UnrealisedPnL'] = (df['MarketValue'] - df['Price']) * df['Quantity']
    df['UnrealisedPnLPercentage'] = round(((df['MarketValue']-df['Price'])/df['Price'])*100,2)
    return df

def getUserPortfolio(portfolioId, df=all_df):
    user_df = df[df["PortfolioId"]==portfolioId]
    return user_df.to_json(orient="records")

def getAllPorfolioRefresh(df=all_df):
    df = retrieveStockUpdates(df)
    #add code to update to database
    return df.to_json(orient="records")

def getAllPorfolio(df=all_df):
    return df.to_json(orient="records")


def addUserTicker(portfolioId, ticker, quantity, price):
    stockData = yf.Ticker(ticker)

    if stockData.info['regularMarketPrice'] == None:
        return "Invalid Stock ticker"
    else:
        newTicker = {
            "PortfolioId":portfolioId, 
            "Ticker": stockData.info['symbol'], 
            "Quantity": quantity, 
            "Price": price,
            "Name": stockData.info['shortName'],
            "MarketValue": stockData.info['regularMarketPrice'],
            "UnrealisedPnL": (stockData.info['regularMarketPrice']-price) * quantity,
            "UnrealisedPnLPercentage": round(((stockData.info['regularMarketPrice']-price)/price)*100,2)
        }
        #add code to add stocks into db
       
        return "Success"


if __name__ == "__main__":
    # print(stockInfo("aapl"))
    # print(stockInfo("12345"))
    # print(portfolioInfo(2))   
    # print(getUserPortfolio(1))     
    # getAllPorfolioRefresh()
    
    addUserTicker("2", "AMC", 1000, 24.44)
    # getAllPorfolio(all_df)
