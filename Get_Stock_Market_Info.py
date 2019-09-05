# The APIs used to collect data are "alphavantage" and "quandl"
# from libraries
import requests
import pandas as pd
import json
import os
import quandl
import time

# from files:
import auth
import params
import sp_500_companies

# url_base:
alpha_vantage_base = "https://www.alphavantage.co"
raw_data_folder = "C:/Users/John Xu/Desktop/Stock_Market_Trend_Prediction/AlphaVantage_data/"
# initialization:
stock_symbols = sp_500_companies.ticker_list
# Extract 20-year historical data for ETF that correspond to Dow Jones, S&P 500, Gold, US Bond Market, and US Dollar
# Index


def get_alpha_vantage_data(symbols):
    param_dict_names = [name for name in dir(params) if ('params' in name)]
    param_dict_keys = [key.replace('_params', '') for key in dir(params) if ('params' in key)]
    param_dict = {key: getattr(params, name) for key in param_dict_keys for name in param_dict_names}
    for stock_symbol in symbols:
        print('Getting data for {}...'.format(stock_symbol))
        for param_name, param_value in param_dict.items():
            print("Process Begin...")
            param_value["symbol"] = stock_symbol
            r = requests.get(alpha_vantage_base + '/query', params=param_value)
            content = json.loads(r.content)
            fund_prefix = ''.join((stock_symbol, "_"))
            file_name = ''.join((fund_prefix, (param_name + '.json')))
            with open(os.path.join(raw_data_folder, file_name), "w") as fp:
                json.dump(content, fp)
            print("Successfully extracted {}!".format(file_name))
            print("Process halting...")
            time.sleep(20)
        print("Data extraction for {} complete!".format(stock_symbol))

    print('Alpha Vantage Data Extraction Process Complete!!')


get_alpha_vantage_data(symbols=stock_symbols)
