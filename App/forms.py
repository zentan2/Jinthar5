from flask_wtf import FlaskForm 
from App.models import Portfolio, User
from wtforms import StringField, IntegerField, SubmitField, BooleanField
from wtforms.validators import Required

class StockUpdate(FlaskForm):
    name = StringField('Name', validators=[Required()])
    ticker = StringField('Ticker', validators=[Required()])
    country = StringField('Country', validators=[Required()])
    cost = IntegerField("Cost Price", validators=[Required()])
    quantity = IntegerField("Quantity", validators=[Required()])
    submit = SubmitField('Update')

class StockAdd(FlaskForm):
    name = StringField('Name', validators=[Required()])
    ticker = StringField('Ticker', validators=[Required()])
    country = StringField('Country', validators=[Required()])
    cost = IntegerField("Cost Price", validators=[Required()])
    quantity = IntegerField("Quantity", validators=[Required()])
    submit = SubmitField('Add')

class StockRemove(FlaskForm):
    name = StringField('Name', validators=[Required()])
    ticker = StringField('Ticker', validators=[Required()])
    submit = SubmitField('Delete')