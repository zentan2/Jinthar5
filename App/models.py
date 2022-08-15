from app import db

class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Ticker = db.Column(db.String(20), nullable=False)
    Quantity = db.Column(db.Integer, nullable=False)
    Price = db.Column(db.Numeric(10,2), nullable=False)
    Name = db.Column(db.String(200), nullable=False)
    Country = db.Column(db.String(50), nullable=False)
    MarketValue = db.Column(db.Numeric(10,2), nullable=False)
    UnrealisedPnL = db.Column(db.Numeric(10,2), nullable=False)
    UnrealisedPnLPercentage = db.Column(db.Numeric(10,2), nullable=False)

    def __repr__(self):
        return '<Portfolio {}>'.format(self.Ticker)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)
 