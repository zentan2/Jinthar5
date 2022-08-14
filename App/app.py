from flask import Flask, request, jsonify
from Service import stocksData
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#retrieving df and data from login
# testing code


@app.route("/") #This is the route to the home page
def index():
    return "This is the homepage"

@app.route("/api/stocks/<ticker>", methods=["POST", "GET"])
def stock(ticker):
    return f"{stocksData.stockInfo(ticker)}"

@app.route("/api/portfolio", methods=["GET"])
def allPortfolio():
    return f'{stocksData.getAllPorfolio()}'

@app.route("/api/portfolio/refresh", methods=["GET"])
def allPortfolioRefresh():
    return f'{stocksData.getAllPorfolioRefresh()}'

@app.route("/api/portfolio/<userId>", methods=["POST", "GET"])
def portfolio(userId):
    return f'{stocksData.getUserPortfolio(int(userId))}'

@app.route("/api/portfolio/test", methods=["POST", "GET"])
def portfolioAdd():
    data = request.json
    return print(jsonify(data))

# driver function
if __name__ == '__main__':
    app.run(debug = True)