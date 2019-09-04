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

index_fund_params = params.index_fund_params
sma_open_params = params.sma_open_params
sma_close_params = params.sma_close_params
ema_open_params = params.ema_open_params
ema_close_params = params.ema_close_params
macd_open_params = params.macd_open_params
macd_close_params = params.macd_close_params
stoch_params = params.stoch_params
rsi_open_params = params.rsi_open_params
rsi_close_params = params.rsi_close_params
adx_params = params.adx_params
mom_open_params = params.mom_open_params
mom_close_params = params.mom_close_params
bop_params = params.bop_params
cci_params = params.cci_params
roc_open_params = params.roc_open_params
roc_close_params = params.roc_close_params
aroon_params = params.aroon_params
mfi_params = params.mfi_params
dx_params = params.dx_params
bbands_open_params = params.bbands_open_params
bbands_close_params = params.bbands_close_params
sar_params = params.sar_params
trange_params = params.trange_params
ad_params = params.ad_params
obv_params = params.obv_params
ht_trendline_open_params = params.ht_trendline_open_params
ht_trendline_close_params = params.ht_trendline_close_params

param_dict = {"index_fund": index_fund_params, "sma_open":sma_open_params, "sma_close": sma_close_params, "ema_open": ema_open_params,
              "ema_close": ema_close_params, "macd_open": macd_open_params, "macd_close": macd_close_params, "stoch": stoch_params,
              "rsi_open": rsi_open_params, "rsi_close": rsi_close_params, "adx": adx_params, "mom_open": mom_open_params,
              "mom_close": mom_close_params, "bop": bop_params, "cci": cci_params, "roc_open": roc_open_params, "roc_close": roc_close_params,
              "aroon": aroon_params, "mfi": mfi_params, "dx": dx_params, "bbands_open": bbands_open_params, "bbands_close": bbands_close_params,
              "sar": sar_params, "trange": trange_params, "ad": ad_params, "obv": obv_params, "ht_trendline_open": ht_trendline_open_params,
              "ht_trendline_close": ht_trendline_close_params}


def get_alpha_vantage_data(stock_symbols, param_dict):
    for fund in fund_symbols:
        print('Getting data for {}...'.format(fund))
        for param_name, param_value in param_dict.items():
            print("Process Begin...")
            param_value["symbol"] = fund
            r = requests.get(alpha_vantage_base + '/query', params=param_value)
            content = json.loads(r.content)
            fund_prefix = ''.join((fund, "_"))
            file_name = ''.join((fund_prefix, (param_name + '.json')))
            with open(os.path.join(raw_data_folder, file_name), "w") as fp:
                json.dump(content, fp)
            print("Successfully extracted {}!".format(file_name))
            print("Process halting...")
            time.sleep(20)
        print("Data extraction for {} complete!".format(fund))

    print('Alpha Vantage Data Extraction Process Complete!!')

get_alpha_vantage_data(stock_symbols=stock_symbols, param_dict=param_dict)
