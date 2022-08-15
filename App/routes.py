from flask import Flask, request, jsonify
import json
import pandas as pd
from app import app
import yfinance as yf

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


@app.route("/") #This is the route to the home page
def index():
    return "This is the homepage"

@app.route("/api/stocks/<ticker>", methods=["POST", "GET"])
def stockInfo(ticker):
    #obtains information of a single stock
    stockData = yf.Ticker(ticker)
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

@app.route("/api/portfolio", methods=["GET"])
def getAllPorfolio(df=all_df):
    return df.to_json(orient="records")

@app.route("/api/portfolio/<Id>", methods=["POST", "GET"])
def getUserPortfolio(Id, df=all_df):
    temp_df = df[df['PortfolioId'] == int(Id)]
    return temp_df.to_json(orient="records")

@app.route("/api/portfolio/refresh", methods=["GET"])
def getAllPorfolioRefresh(df=all_df):
    df = retrieveStockUpdates(df)
    #add code to update to database
    return df.to_json(orient="records")

# driver function
if __name__ == '__main__':
    app.run(debug = True)