from http.client import NOT_EXTENDED
from traceback import print_last
import pandas as pd
from .models import Portfolio
import yfinance as yf
import json
import pandas as pd
from flask import Flask, request, jsonify
from App import db
from sqlalchemy import select, text, column

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
            "dailyPnL": round((stockData.info["regularMarketPrice"] - stockData.info["previousClose"]),2),
            "dailyPnLPercentage": round(((stockData.info["regularMarketPrice"] - stockData.info["previousClose"]) / stockData.info["previousClose"])*100,2),
        }
    return stockDictionary

def getAllPorfolio():
    return jsonify({"Portfolio":[stocks.json() for stocks in Portfolio.query.all()]}), 200

def getUserPortfolio(Country):
    return jsonify({"Portfolio":[stocks.json() for stocks in Portfolio.query.filter_by(Country=Country.upper())]}), 200

def getPortfolioTotal(Country):
    portfolioTotal = 0
    total = [float(stocks.getUnrealisedPnL()) for stocks in Portfolio.query.filter_by(Country=Country.upper())]
    return jsonify({"Country": Country.upper(), "PortfolioUnrealisedPnLTotal":round(sum(total),2)})

def getPortfolioTotal2(Country):
    portfolioUnrealised = 0
    portfolioPnL = 0
    portfolioMarketValue = 0
    for stocks in Portfolio.query.filter_by(Country=Country.upper()):
        portfolioUnrealised+=float(stocks.getUnrealisedPnL())
        portfolioPnL+=float(stocks.getDailyPnL())
        portfolioMarketValue+=float(stocks.getMarketValue())

    return jsonify({"Country": Country.upper(), "PortfolioUnrealisedPnLTotal":round(portfolioUnrealised,2), "PortfolioDailyPnLTotal": round(portfolioPnL,2), "PortfolioMarketValueTotal": round(portfolioMarketValue,2)})

def getPortfolioDaily(Country):
    portfolioTotal = 0
    total = [float(stocks.getDailyPnL()) for stocks in Portfolio.query.filter_by(Country=Country.upper())]
    return jsonify({"Country": Country.upper(), "PortfolioDailyPnLTotal":round(sum(total),2)})

def getPortfolioStock(ticker):
    stock = Portfolio.query.filter_by(Ticker=ticker.upper())
    stockList = [stocks.json() for stocks in Portfolio.query.filter_by(Ticker=ticker.upper())]
    if len(stockList) == 0:
        return "Stock not found in portfolio"
    else:
        return stockList[0]
    
def getDf():
    df = pd.DataFrame([stocks.json() for stocks in Portfolio.query.all()])
    return df

def populatePortfolioInfo(portfolios):
    # obtains stock information for all the stocks in the list
    ###  change to retrieve data from sql!
    portfolio = {}
    tickers = yf.Tickers(" ".join(portfolios))

    for stockTicker, stockInfo in tickers.tickers.items():
        portfolio[stockTicker] = {
            "name":stockInfo.info['shortName'],
            "currentPrice":round(float(stockInfo.info['regularMarketPrice']),2),
            "dailyPnL": round((stockInfo.info["regularMarketPrice"] - stockInfo.info["previousClose"]),2),
            "dailyPnLPercentage": round(((stockInfo.info["regularMarketPrice"] - stockInfo.info["previousClose"]) / stockInfo.info["previousClose"])*100,2),
            "country": (stockInfo.info["currency"])
        }
    print("retrieval from yfinance completed")  
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

def refreshPortfolio():
    for stockObjects in Portfolio.query.all():
        stock = stockObjects.json()
        ticker = stock['Ticker']
        quantity = stock['Quantity']
        price = stock['Price']
        stock = newTickerInfo(ticker, int(quantity), float(price))
        Portfolio.query.filter_by(Ticker=ticker).update(stock)
        db.session.commit()
    
    return "success"

def newTickerInfo(ticker, quantity, price):
    stockData = yf.Ticker(ticker)

    if stockData.info['regularMarketPrice'] == None:
        return "Invalid Stock ticker"
    else:
        newTicker = {
            "Ticker": stockData.info['symbol'], 
            "Quantity": quantity, 
            "Price": price,
            "Name": stockData.info['shortName'],
            "Country": stockData.info['currency'],
            "MarketValue": round(stockData.info['regularMarketPrice'],2),
            "UnrealisedPnL": round(((stockData.info['regularMarketPrice']-price) * quantity),2),
            "UnrealisedPnLPercentage": round(((stockData.info['regularMarketPrice']-price)/price)*100,2),
            "DailyPnL": round((stockData.info["regularMarketPrice"] - stockData.info["previousClose"]),2),
            "DailyPnLPercentage": round(((stockData.info["regularMarketPrice"] - stockData.info["previousClose"]) / stockData.info["previousClose"])*100,2)
        }
        return newTicker

def addStock(ticker, quantity, price, country):
    if country.upper() == "SGD":
        if ".SI" not in ticker.upper():
            ticker += ".si"
    newStock = newTickerInfo(ticker, quantity, price)
    if newStock == "Invalid Stock ticker":
        return newStock
    else:
        print(newStock)
        portfolioObject = Portfolio(
            Ticker = newStock['Ticker'], 
            Quantity = newStock['Quantity'],
            Price = newStock['Price'], 
            Name = newStock['Name'], 
            Country = newStock['Country'], 
            MarketValue = newStock['MarketValue'], 
            DailyPnL = newStock['DailyPnL'], 
            DailyPnLPercentage = newStock['DailyPnLPercentage'], 
            UnrealisedPnL = newStock['UnrealisedPnL'], 
            UnrealisedPnLPercentage = newStock['UnrealisedPnLPercentage']
            )
        db.session.add(portfolioObject)
        db.session.commit()
        
    return "success"

def deleteStock(ticker, country):
    if country.upper() == "SGD":
        ticker += ".si"

    stock = [stock.json() for stock in Portfolio.query.filter_by(Ticker=ticker.upper())]
    if len(stock) == 0:
        return "Stock not found in portfolio"
    else:
        Portfolio.query.filter_by(Ticker=ticker.upper()).delete()
        db.session.commit()
        return "Success", 200
   