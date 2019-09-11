# The APIs used to collect data are "alphavantage" and "quandl"
# from libraries
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import pandas as pd
import dask.dataframe as dd
from io import StringIO
import quandl
import time
import boto3
import datetime

# from files:
import auth
import params


# raw_data_folder = "C:/Users/John Xu/Desktop/Stock_Market_Trend_Prediction/AlphaVantage_data/"
# initialization:
# stock_symbols = sp_500_companies.ticker_list


# Extract 20-year historical data for ETF that correspond to Dow Jones, S&P 500, Gold, US Bond Market, and US Dollar
# Index


def get_alpha_vantage_data(symbols):
    begin_time = time.perf_counter()
    stock_info_list = []
    alpha_vantage_base = "https://www.alphavantage.co"  # url base
    param_dict_names = [name for name in dir(params) if ('_params' in name)]
    param_dict_list = [getattr(params, name) for name in param_dict_names]
    for stock_symbol in symbols:
        stock_indicators = []
        start = time.perf_counter()
        for i in range(len(param_dict_list)):
            session = requests.Session()
            retry = Retry(connect=5, backoff_factor=0.5)
            adapter = HTTPAdapter(max_retries=retry)
            session.mount("http://", adapter)
            session.mount("https://", adapter)
            param_dict_list[i]["symbol"] = stock_symbol
            r = session.get(alpha_vantage_base + '/query', params=param_dict_list[i], headers=auth.user_agent)
            df = pd.read_csv(StringIO(r.content.decode('utf-8')), engine="python").loc[1:,:]
            df.columns = [param_dict_list[i]["function"] + "_" + str(column) for column in df.columns]
            df.set_index(df.columns[0], inplace=True)
            if param_dict_list[i]["function"] == "TIME_SERIES_DAILY_ADJUSTED":
                df["stock_symbol"] = stock_symbol
            stock_indicators.append(df)
            print("Successfully extracted {}!".format(stock_symbol + "_" + param_dict_names[i].replace("_params", "")))
        stock_info = pd.concat(stock_indicators, axis=1, sort=False)
        stock_info = stock_info.loc[:, ~stock_info.columns.duplicated()]
        stock_info_list.append(stock_info)
        runtime = time.perf_counter() - start
        print("Data extraction for {} complete! Runtime:{} seconds".format(stock_symbol, str(round(runtime, 2))))
        print("Total Time Elapsed--{} seconds...".format(str(round(time.perf_counter() - begin_time, 2))))

    concat_data = pd.concat(stock_info_list, axis=0, sort=False)
    total_runtime = time.perf_counter() - begin_time
    print('Alpha Vantage Data Extraction Process Complete!!  Total Runtime: {} seconds...'.format(str(total_runtime)))
    return concat_data


def get_quandl_data(quandl_params):  # indicators are a list of the names of external indicators
    quandl.ApiConfig.api_key = auth.apikey_quandl
    indicator_data_list = []
    begin_time = time.perf_counter()
    print("Begin Retrieving Quandl Data...")
    for param in quandl_params:
        dict_ = getattr(params, param)
        data = quandl.get("{}/{}".format(dict_["database_code"], dict_["dataset_code"]),
                          start_date=dict_["start_date"], end_date=dict_["end_date"])
        # data = data.add_prefix(param.split("_")[0]+"_")
        data.columns = [param.split("_")[0] + "_" + str(column) for column in data.columns]
        indicator_data_list.append(data)
        print("Retrieved Data on {}! Time Elapsed: {} seconds".format(param.replace("_parameters", ""),
                                                                      str(round(time.perf_counter() - begin_time))))
    indicator_data = pd.concat(indicator_data_list, axis=1, sort=False)
    print("Process Complete!!!")
    return indicator_data


def write_data_to_s3(df, bucket_name, file_name):
    csv_buffer = StringIO()
    df.to_csv(csv_buffer)
    s3_resource = boto3.resource('s3')
    s3_resource.Object(bucket_name, '{}.csv'.format(file_name)).put(Body=csv_buffer.getvalue())
