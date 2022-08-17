from flask import Flask, request, jsonify, flash
from App import app
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

@app.route('/api/portfolio/add',methods=['GET','POST'])
def addStock():
    ticker = request.form["ticker"]
    price = float(request.form["price"]) 
    quantity = float(request.form["quantity"])
    country = request.form['country']
    return processing.addStock(ticker, quantity, price, country)