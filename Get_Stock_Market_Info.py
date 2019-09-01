#from libraries
import requests
import pandas as pd
import pickle
import json


#from files:
import auth

# url_base:
alpha_vantage_base = "https://www.alphavantage.co"

#initialization:
fund_symbols = ['VFINX', 'VTSMX', 'FXAIX', 'SWTSX']
#Extract 20-year historical data for ETF that correspond to Dow Jones, S&P 500, Gold, US Bond Market, and US Dollar Index
technical_indicators = ['SMA', 'EMA', 'MACD', 'STOCH', 'RSI', 'ADX', 'MOM', 'BOP', 'CCI', 'ROC', 'AROON', 'MFI',
                        'DX', 'BBANDS', 'AD', 'OBV']




def get_index_trend(fund_symbols, outputsize, apikey):
    for fund in fund_symbols:
        print('Getting 20-year daily historical data for {}'.format(fund))
        params = {
            "function": "Time_Series_Daily",
            "symbol": fund,
            "outputsize": outputsize,
            "datatype": "json",
            "apikey": apikey
        }
        r = requests.get(alpha_vantage_base + '/query', params=params)
        time_series_daily = pd.DataFrame.from_dict(json.loads(r.content)['Time Series (Daily)'], orient='index')
        return time_series_daily

VFINX, VTSMX, FXAIX, SWRSX = get_index_trend(fund_symbols=fund_symbols, outputsize='full', apikey=auth.apikey)


def get_indicators():
    
