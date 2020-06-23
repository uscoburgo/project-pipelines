import pandas as pd
import numpy as np
import re
import requests
from bs4 import BeautifulSoup
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import os
from dotenv import load_dotenv
load_dotenv()

def plotSentiment(df):
    plot = df.groupby("Ticker").agg({"positive_sentiment": "sum","negative_sentiment":"sum"}).plot.bar(rot=0)
    fig = plot.get_figure()
    fig.savefig('../OUTPUT/plot.jpg')
    return plot


def plotStockPrice(stock=None):
    key = os.getenv("ALPHAVANTAGE_APIKEY")
    ts = TimeSeries(key, output_format='pandas')
    data1, meta_data = ts.get_intraday(symbol=f'{stock}',interval='1min', outputsize='full')
    data1['4. close'].plot()
    plt.title(f'Intraday Times Series for the {stock} stock (1 min)')
    plot = plt.show()
    fig = plot.get_figure()
    fig.savefig('../OUTPUT/plot_stock.jpg')
    return plot