import sqlite3
from App import db

class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Ticker = db.Column(db.String(20), nullable=False)
    Quantity = db.Column(db.Integer, nullable=False)
    Price = db.Column(db.Numeric(10,2), nullable=False)
    Name = db.Column(db.String(200), nullable=False)
    Country = db.Column(db.String(50), nullable=False)
    MarketValue = db.Column(db.Numeric(10,2), nullable=False)
    DailyPnL = db.Column(db.Numeric(10,2), nullable=False)
    DailyPnLPercentage = db.Column(db.Numeric(10,2), nullable=False)
    UnrealisedPnL = db.Column(db.Numeric(10,2), nullable=False)
    UnrealisedPnLPercentage = db.Column(db.Numeric(10,2), nullable=False)

    def json(self):
        return{
            "id": self.id, 
            "Ticker": self.Ticker, 
            "Quantity": self.Quantity, 
            "Price": self.Price, 
            "Name": self.Name, 
            "Country": self.Country, 
            "MarketValue": self.MarketValue, 
            "DailyPnL": self.DailyPnL, 
            "DailyPnLPercentage": self.DailyPnLPercentage, 
            "UnrealisedPnL": self.UnrealisedPnL, 
            "UnrealisedPnLPercentage":self.UnrealisedPnLPercentage
            }
    def getTickers(self):
        return self.Ticker

    def getUnrealisedPnL(self):
        return self.UnrealisedPnL

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)
 

#  sample data to be added into sql
#  INSERT INTO portfolio (
# Ticker, Quantity, Price, Name, Country, MarketValue, DailyPnL, DailyPnLPercentage, UnrealisedPnL, UnrealisedPnLPercentage 
# )
# VALUES
# ("OV8.SI",10000,1.65,"Sheng Siong","SGD",1.62,0.02,1.25,-300.0,-1.82),
# ("G3B.SI",20000,3.31,"Nikko AM STI ETF","SGD",3.34,0.01,0.30,600.0,0.91),
# ("D05.SI",8000,31.97,"DBS","SGD",32.80,-0.19,-0.58,6640.0,2.60),
# ("U11.SI",16000,25.30,"UOB","SGD",27.20,-0.12,-0.44,30400.0,7.51),
# ("NVDA",100,177.22,"NVIDIA Corporation","USD",190.32,3.23,1.73,1310.0,7.39),
# ("META",20,170.50,"Meta Platforms, Inc.","USD",180.89,0.39,0.22,207.8,6.09),
# ("INTC",50,38.22,"Intel Corporation","USD",36.34,0.23,0.64,-94.0,-4.92),
# ("SPY",10,410.22,"SPDR S&P 500","USD",428.86,1.76,0.41,186.4,4.54),
# ("AAPL",20,120.50,"Apple Inc.","USD",173.19,1.09,0.63,1053.8,43.73);