# download stock prices from yahoo finance

import pandas_datareader as pdr
import datetime as dt

print("starting download ...")
tickers1 = ['BABA', 'PDD', 'JD', 'BIDU', 'NTES', 'NIO', 'BILI', 'TME', 'EDU', 'YUMC', 'TCOM', 'ZTO', 'AMZN', 'TSLA', 'UL', 'JNJ']
df1 = pdr.data.get_data_yahoo(tickers1, start = dt.datetime(2020, 4, 2), end = dt.datetime(2021, 4, 1))['Adj Close']
df1.to_csv("data/example_prices.csv")

print("completed download")


