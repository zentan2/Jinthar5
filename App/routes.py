from flask import Flask, request, jsonify, flash
from App import app
from .models import Portfolio
from . import processing


@app.route("/") #This is the route to the home page
def index():
    return "Service is running"

@app.route("/api/stocks/<ticker>", methods=["POST", "GET"])
def stock_Info(ticker):
    return jsonify(processing.stockInfo(ticker))

@app.route("/api/portfolio", methods=["GET"])
def getAll_Porfolio():
    return processing.getAllPorfolio()

@app.route("/api/portfolio/<Country>", methods=["POST", "GET"])
def getUser_Portfolio(Country):
    return processing.getUserPortfolio(Country)

@app.route("/api/portfolio/total/<Country>", methods=["POST", "GET"])
def getPortfolioTotal(Country):
    return processing.getPortfolioTotal2(Country)

@app.route("/api/portfolio/daily/<Country>", methods=["POST", "GET"])
def getPortfolioDaily(Country):
    return processing.getPortfolioDaily(Country)

@app.route("/api/portfolio/stock/<ticker>", methods=["POST", "GET"])
def getPortfolioStock(ticker):
    return processing.getPortfolioStock(ticker)

@app.route('/api/portfolio/add',methods=['GET','POST'])
def addStock():
    ticker = request.json['ticker']
    price = float(request.json["price"]) 
    quantity = float(request.json["quantity"])
    country = request.json['country']
    return processing.addStock(ticker, quantity, price, country)

@app.route('/api/portfolio/update',methods=['GET','POST'])
def updateStock():
    ticker = request.json['ticker']
    price = float(request.json["price"]) 
    quantity = float(request.json["quantity"])
    country = request.json['country']
    return processing.updateStock(ticker, quantity, price, country)

@app.route('/api/portfolio/delete',methods=['GET','POST'])
def removeStock():
    ticker = request.json["ticker"]
    country = request.json['country']
    return processing.deleteStock(ticker, country)

@app.route('/api/portfolio/refresh',methods=['GET'])
def updatePortfolio():
    return processing.refreshPortfolio()

@app.route('/api/portfolio/deleteTest',methods=['GET','POST'])
def removeStock2():
    ticker = request.json["ticker"]
    country = request.json['country']
    return processing.deleteStock(ticker, country)