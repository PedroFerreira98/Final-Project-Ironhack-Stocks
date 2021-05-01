#import pandas as pd
#import requests
import yfinance as yf
#from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

'''
msft = yf.Ticker("MSFT")
hist = msft.history(period="5y")

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-historical-data"

querystring = {"symbol":"AMRN","region":"US"}

headers = {
    'x-rapidapi-key': "8a36ce004emsh8cadb6a3ca2130ap1d64e8jsn114b8aab7356",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

results = response.json()
results['prices']
#flattened_data = json_normalize(results)

#flattened_data
df = pd.DataFrame(results['prices'])
'''

# Choose Ticker to analyse
msft = yf.Ticker("MSFT")

# Stock price daily from 1year back from now
stock_price_daily = yf.download(
    # tickers list or string as well
    #tickers="SPY AAPL MSFT",
    tickers='MSFT',

    # use "period" instead of start/end
    # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    # (optional, default is '1mo')
    period="5y",

    # group by ticker (to access via data['SPY'])
    # (optional, default is 'column')
    group_by='ticker',

    # adjust all OHLC automatically
    # (optional, default is False)
    auto_adjust=True,

    # download pre/post regular market hours data
    # (optional, default is False)
    prepost=True,

    # use threads for mass downloading? (True/False/Integer)
    # (optional, default is True)
    threads=True,

    # proxy URL scheme use use when downloading?
    # (optional, default is None)
    proxy=None
)


# In case I download more than one ticker at a time, I'll have to stack because it creates multivel columns
#stock_price_daily = stock_price_daily.stack(level=0).rename_axis(['Date', 'Ticker']).reset_index(level=1)

stock_price_daily = stock_price_daily.reset_index().rename(columns={'index': 'Date'})

# Annual Balance sheet for Microsoft
balance = msft.balance_sheet
# Get main ratios of microsoft
info = msft.info



#msft_prices = stock_price_daily[stock_price_daily['Ticker'] == 'MSFT']

# Chart for Closing Prices of Microsoft
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.plot(stock_price_daily.Date, stock_price_daily.Close)
plt.title('MSFT Chart')
plt.xlabel('Date')
plt.ylabel('Price')
plt.yticks(np.arange(min(stock_price_daily.Close), max(stock_price_daily.Close), step=20))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=4))
plt.xticks(rotation=45)
#fmt_month = mdates.MonthLocator()
#ax.xaxis.set_minor_locator(fmt_month)
plt.show()


#returns only "Close" collum
def stock_close():
    data = stock_price_daily.iloc[:,2:3].values
    return data

#Returns dataframe with Open,Close, High, Low and Volume
def stock_values():
    data = stock_price_daily
    return data