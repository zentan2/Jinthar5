from flask import Flask, request, jsonify, flash
import json
import pandas as pd
from App import app, db
import yfinance as yf
from App.forms import (StockUpdate, StockAdd, StockRemove)
from .models import Portfolio

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
def getAllPorfolio():
    return jsonify({"Portfolio":[stocks.json() for stocks in Portfolio.query.all()]}), 200

@app.route("/api/portfolio/<Country>", methods=["POST", "GET"])
def getUserPortfolio(Country):
    return jsonify({"Portfolio":[stocks.json() for stocks in Portfolio.query.filter_by(Country=Country.upper())]}), 200

# @app.route("/api/portfolio/refresh", methods=["GET"])
# def getAllPorfolioRefresh(df=all_df):
#     df = retrieveStockUpdates(df)
#     #add code to update to database
#     return df.to_json(orient="records")

@app.route('/api/portfolio/add',methods=['GET','POST'])
def addStock():
    addStockForm = StockAdd()
    if addStockForm.validate_on_submit():
        stock_add = Portfolio(name=addStockForm.name.data, ticker=addStockForm.ticker.data, country=addStockForm.country.data, cost=addStockForm.cost.data, quantity=addStockForm.quantity.data)
        db.session.add(stock_add)
        db.session.commit()
        flash('Your stock has been added', 'success')
    return render_template('successfuladdstock.html', form=addStockForm) 
