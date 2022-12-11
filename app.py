from flask import Flask, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap


import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from stock_data import stock_data

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/calculate', methods =['POST', 'GET'])
def calc():

    if request.method == 'POST':
        ticker = request.form['Ticker']
        return redirect(url_for("ticker", ticker=ticker))

    return render_template("calculate.html")

@app.route('/methods')
def method():

    return render_template("methods.html")

@app.route('/<ticker>', methods =['POST', 'GET'])
def ticker(ticker):

    stock = stock_data(ticker)
    prediction = stock.get_prediction()

    if prediction != None:
        stock.history_graph()
        prediction = round(prediction,4)*100

        return render_template("results.html", prediction = prediction, ticker = ticker)
    else:

        return render_template("no_result.html")

