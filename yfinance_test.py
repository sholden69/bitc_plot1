import numpy as np
import pandas as pd
#Data Source
import yfinance as yf

aapl= yf.Ticker("aapl")
aapl
aapl_historical = aapl.history(start="2021-01-01", end="2021-05-01", interval="1wk")
aapl_historical