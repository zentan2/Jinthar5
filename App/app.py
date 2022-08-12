from flask import Flask, request
from Service import stocksData
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/") #This is the route to the home page
def hello_world():
    return "This is the homepage"

@app.route("/api/stocks/<ticker>", methods=["POST", "GET"])
def stock(ticker):
    return f"{stocksData.stockInfo(ticker)}"

@app.route("/api/portfolio/<number>", methods=["POST", "GET"])
def portfolio(number):
    return f'{stocksData.portfolioInfo(number)}'

# driver function
if __name__ == '__main__':
    app.run(debug = True)