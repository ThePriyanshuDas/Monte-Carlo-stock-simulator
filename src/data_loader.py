import pandas as pd
import yfinance as yf

def load_csv(path):
    return pd.read_csv(path, index_col=0, parse_dates=True)

def load_from_yahoo(ticker, start="2020-01-01"):
    data = yf.download(ticker, start=start)
    return data["Close"]