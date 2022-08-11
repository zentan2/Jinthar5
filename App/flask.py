from flask import Flask, request

app = Flask(__name__)

@app.route("/") #This is the route to the home page
def hello_world():
    return "This is the homepage"

# @app.route("/search", methods=['POST']) #this page allows you to submit stock tickers
# def searchTickers():
#     tickers = []
#     tickers = request.get_json().split()
#     return tickers



# driver function
if __name__ == '__main__':
    app.run(debug = True)