from flask import Flask, request, jsonify
import json
import pandas as pd
from app import app
import yfinance as yf

stocks = [
    {"PortfolioId":1,"Ticker":"OV8.SI","Quantity":10000,"Price":1.65,"Name":"Sheng Siong","MarketValue":1.62,"UnrealisedPnL":-300.0,"UnrealisedPnLPercentage":-1.82,"country":"SGD","DailyPnL":0.02,"DailyPnLPercentage":1.25},
    {"PortfolioId":1,"Ticker":"G3B.SI","Quantity":20000,"Price":3.31,"Name":"Nikko AM STI ETF","MarketValue":3.34,"UnrealisedPnL":600.0,"UnrealisedPnLPercentage":0.91,"country":"SGD","DailyPnL":0.01,"DailyPnLPercentage":0.3},
    {"PortfolioId":1,"Ticker":"D05.SI","Quantity":8000,"Price":31.97,"Name":"DBS","MarketValue":32.8,"UnrealisedPnL":6640.0,"UnrealisedPnLPercentage":2.6,"country":"SGD","DailyPnL":-0.19,"DailyPnLPercentage":-0.58},
    {"PortfolioId":1,"Ticker":"U11.SI","Quantity":16000,"Price":25.3,"Name":"UOB","MarketValue":27.2,"UnrealisedPnL":30400.0,"UnrealisedPnLPercentage":7.51,"country":"SGD","DailyPnL":-0.12,"DailyPnLPercentage":-0.44},
    {"PortfolioId":2,"Ticker":"nvda","Quantity":100,"Price":177.22,"Name":"NVIDIA Corporation","MarketValue":190.32,"UnrealisedPnL":1310.0,"UnrealisedPnLPercentage":7.39,"country":"USD","DailyPnL":3.23,"DailyPnLPercentage":1.73},
    {"PortfolioId":2,"Ticker":"meta","Quantity":20,"Price":170.5,"Name":"Meta Platforms, Inc.","MarketValue":180.89,"UnrealisedPnL":207.8,"UnrealisedPnLPercentage":6.09,"country":"USD","DailyPnL":0.39,"DailyPnLPercentage":0.22},
    {"PortfolioId":2,"Ticker":"intc","Quantity":50,"Price":38.22,"Name":"Intel Corporation","MarketValue":36.34,"UnrealisedPnL":-94.0,"UnrealisedPnLPercentage":-4.92,"country":"USD","DailyPnL":0.23,"DailyPnLPercentage":0.64},
    {"PortfolioId":2,"Ticker":"spy","Quantity":10,"Price":410.22,"Name":"SPDR S&P 500","MarketValue":428.86,"UnrealisedPnL":186.4,"UnrealisedPnLPercentage":4.54,"country":"USD","DailyPnL":1.76,"DailyPnLPercentage":0.41},
    {"PortfolioId":2,"Ticker":"aapl","Quantity":20,"Price":120.5,"Name":"Apple Inc.","MarketValue":173.19,"UnrealisedPnL":1053.8,"UnrealisedPnLPercentage":43.73,"country":"USD","DailyPnL":1.09,"DailyPnLPercentage":0.63}
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
            "currentPrice":stockInfo.info['regularMarketPrice'],
            "dailyPnL": stockInfo.info["regularMarketPrice"] - stockInfo.info["previousClose"],
            "dailyPnLPercentage": round(((stockInfo.info["regularMarketPrice"] - stockInfo.info["previousClose"]) / stockInfo.info["previousClose"])*100,2),
            "country": (stockInfo.info["currency"])
        }  
    return portfolio

def retrieveStockUpdates(df):
    tickers = list(set(df['Ticker']))
    updatedPortfolioInfo = populatePortfolioInfo(tickers)
    df['Name'] = df["Ticker"].apply(lambda x : updatedPortfolioInfo[x.upper()]["name"])
    df['MarketValue'] = df["Ticker"].apply(lambda x : updatedPortfolioInfo[x.upper()]["currentPrice"])
    df['country'] = df["Ticker"].apply(lambda x : updatedPortfolioInfo[x.upper()]["country"])
    df['DailyPnL'] = df["Ticker"].apply(lambda x : updatedPortfolioInfo[x.upper()]["dailyPnL"])
    df['DailyPnLPercentage'] = df["Ticker"].apply(lambda x : updatedPortfolioInfo[x.upper()]["dailyPnLPercentage"])
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

