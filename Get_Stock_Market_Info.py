# The APIs used to collect data are "alphavantage" and "quandl"
# from libraries
import requests
import pandas as pd
import pickle
import json
import quandl

# from files:
import auth
import params

# url_base:
alpha_vantage_base = "https://www.alphavantage.co"

# initialization:
fund_symbols = ['VFINX', 'VTSMX', 'FXAIX', 'SWTSX']
# Extract 20-year historical data for ETF that correspond to Dow Jones, S&P 500, Gold, US Bond Market, and US Dollar
# Index
technical_indicators = ['SMA', 'EMA', 'MACD', 'STOCH', 'RSI', 'ADX', 'MOM', 'BOP', 'CCI', 'ROC', 'AROON', 'MFI',
                        'DX', 'BBANDS', 'SAR', 'TRANGE', 'AD', 'OBV']


def get_index_time_series(fund_symbols, outputsize, function, apikey):
    for fund in fund_symbols:
        print('Getting 20-year daily historical data for {}'.format(fund))
        index_params = {
            "function": "Time_Series_Daily",
            "symbol": fund,
            "outputsize": outputsize,
            "datatype": "json",
            "apikey": apikey
        }
        SMA_params = {
            "function": "SMA",
            "symbol": fund,
            "interval": "daily",
            "time_period": 200,
            "series_type": "open",
            "apikey": apikey
        }
        MACD_params = {
            "function": function
        }
        r = requests.get(alpha_vantage_base + '/query', params=index_params)
        time_series_daily = pd.DataFrame.from_dict(json.loads(r.content)['Time Series (Daily)'], orient='index')
        return time_series_daily


VFINX, VTSMX, FXAIX, SWRSX = get_index_time_series(fund_symbols=fund_symbols, outputsize='full', apikey=auth.apikey)


def get_technical_indicators():
    params = {
        "function": function,

    }
