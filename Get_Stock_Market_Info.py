# The APIs used to collect data are "alphavantage" and "quandl"
# from libraries
import requests
import pandas as pd
import json
import os
import quandl
import datetime as dt

# from files:
import auth
import params

# url_base:
alpha_vantage_base = "https://www.alphavantage.co"
raw_data_folder = "C:/Users/John Xu/Desktop/Stock_Market_Trend_Prediction/AlphaVantage_data/"
# initialization:
fund_symbols = ['VFINX', 'VTSMX', 'FXAIX', 'SWTSX']
# Extract 20-year historical data for ETF that correspond to Dow Jones, S&P 500, Gold, US Bond Market, and US Dollar
# Index
technical_indicators = ['SMA', 'EMA', 'MACD', 'STOCH', 'RSI', 'ADX', 'MOM', 'BOP', 'CCI', 'ROC', 'AROON', 'MFI',
                        'DX', 'BBANDS', 'SAR', 'TRANGE', 'AD', 'OBV']

index_fund_params = params.index_fund_params
SMA_open_params = params.SMA_open_params
SMA_close_params = params.SMA_close_params
EMA_open_params = params.EMA_open_params
EMA_close_params = params.EMA_close_params
MACD_open_params = params.MACD_open_params
MACD_close_params = params.MACD_close_params
STOCH_params = params.STOCH_params
RSI_open_params = params.RSI_open_params
RSI_close_params = params.RSI_close_params
ADX_params = params.ADX_params
MOM_open_params = params.MOM_open_params
MOM_close_params = params.MOM_close_params
BOP_params = params.BOP_params
CCI_params = params.CCI_params
ROC_open_params = params.ROC_open_params
ROC_close_params = params.ROC_close_params
AROON_params = params.AROON_params
MFI_params = params.MFI_params
DX_params = params.DX_params
BBANDS_open_params = params.BBANDS_open_params
BBANDS_close_params = params.BBANDS_close_params
SAR_params = params.SAR_params
TRANGE_params = params.TRANGE_params
AD_params = params.AD_params
OBV_params = params.OBV_params
HT_TRENDLINE_open_params = params.HT_TRENDLINE_open_params
HT_TRENDLINE_close_params = params.HT_TRENDLINE_close_params
param_list = [index_fund_params, SMA_open_params, SMA_close_params, EMA_open_params, EMA_close_params,
              MACD_open_params, MACD_close_params, STOCH_params, RSI_open_params, RSI_close_params,
              ADX_params, MOM_open_params, MOM_close_params, BOP_params, CCI_params,
              ROC_open_params, ROC_close_params, AROON_params, MFI_params, DX_params, BBANDS_open_params,
              BBANDS_close_params,
              SAR_params, TRANGE_params, AD_params, OBV_params, HT_TRENDLINE_open_params,
              HT_TRENDLINE_close_params]


def get_alpha_vantage_data(fund_symbols, param_list):
    for fund in fund_symbols:
        print('Getting data for {}...'.format(fund))
        for param in param_list:
            param["symbol"] = fund
            print(param)
            r = requests.get(alpha_vantage_base + '/query', params=param)
            content = json.loads(r.content)
            fund_prefix = ''.join((fund, "_"))
            file_name = ''.join((fund_prefix, (param["function"] + '.json')))
            with open(os.path.join(raw_data_folder, file_name), "w") as fp:
                json.dump(content, fp)
        print("Data extraction for {} complete!".format(fund))


print('Alpha Vantage Data Extraction Process Complete!!')

get_alpha_vantage_data(fund_symbols=fund_symbols, param_list=param_list)
