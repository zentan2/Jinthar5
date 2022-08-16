from flask import Flask, request, jsonify
from App import app
from .models import Portfolio
from . import processing


@app.route("/") #This is the route to the home page
def index():
    return "Service is running"

@app.route("/api/stocks/<ticker>", methods=["POST", "GET"])
def stock_Info(ticker):
    return processing.stockInfo(ticker)

@app.route("/api/portfolio", methods=["GET"])
def getAll_Porfolio():
    return processing.getAllPorfolio()

@app.route("/api/portfolio/<Country>", methods=["POST", "GET"])
def getUser_Portfolio(Country):
    return processing.getUserPortfolio(Country)

# @app.route("/api/portfolio/refresh", methods=["GET"])
# def getAllPorfolioRefresh():
    
    # df = pd.DataFrame([stocks.json() for stocks in Portfolio.query.all()])
    # df = retrieveStockUpdates(df)
    # print(df.head())
    # status = processing.test()
    # return jsonify(status)
#     df = retrieveStockUpdates(df)
#     #add code to update to database
#     return df.to_json(orient="records")