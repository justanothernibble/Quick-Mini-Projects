import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame, Series, read_csv

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

stocks = read_csv('stock_prices.csv')

x = []
for i in range(len(stocks)):
    x.append(stocks.iat[i,0])
y = []
for i in range(len(stocks)):
    y.append(stocks.iat[i,1])

plt.subplot(2,1,1)
plt.title("AAPL")
plt.ylabel("Price")
plt.plot(x)
plt.subplot(2,1,2)
plt.title("MSFT")
plt.ylabel("Price")
plt.plot(y)
plt.show()
