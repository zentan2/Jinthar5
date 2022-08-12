from crypt import methods
from flask import Flask, request
from Service import stocksData

app = Flask(__name__)

@app.route("/") #This is the route to the home page
def hello_world():
    return "This is the homepage"

@app.route("/api/stocks/<ticker>", methods=["POST", "GET"])
def stock(ticker):
    return f"<h1>{stocksData.stockInfo(ticker)}</h1>"


# driver function
if __name__ == '__main__':
    app.run(debug = True)