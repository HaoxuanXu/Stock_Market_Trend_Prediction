# The APIs used to collect data are "alphavantage" and "quandl"
# from libraries
import requests
import pandas as pd
import dask.dataframe as dd
import io
import s3fs
import quandl
import time

# from files:
import auth
import params
import sp_500_companies


raw_data_folder = "C:/Users/John Xu/Desktop/Stock_Market_Trend_Prediction/AlphaVantage_data/"
# initialization:
stock_symbols = sp_500_companies.ticker_list
# Extract 20-year historical data for ETF that correspond to Dow Jones, S&P 500, Gold, US Bond Market, and US Dollar
# Index


def get_alpha_vantage_data(symbols):
    stock_info_list = []
    alpha_vantage_base = "https://www.alphavantage.co"  # url base
    param_dict_names = [name for name in dir(params) if ('params' in name)]
    param_dict = {name: getattr(params, name) for name in param_dict_names}
    param_dict = {name.replace('_params', ''): value for name, value in param_dict.items()}
    for stock_symbol in symbols:
        stock_attribute_df_list = []
        print('Getting data for {}...'.format(stock_symbol))
        for param_name, param_value in param_dict.items():
            print("Process Begin...")
            param_value["symbol"] = stock_symbol
            r = requests.get(alpha_vantage_base + '/query', params=param_value, headers=auth.user_agent)
            df = pd.read_csv(io.StringIO(r.content.decode('utf-8'))).set_index('timestamp')
            if param_name == "stock_time_series":
                df["stock_symbol"] = stock_symbol
            d_df = dd.from_pandas(df, npartitions=5)
            stock_attribute_df_list.append(d_df)

            print("Successfully extracted {}!".format(param_name))
            print("Process halting...")
            time.sleep(20)
        stock_attribute_d = dd.concat(stock_attribute_df_list, axis=1)
        stock_info_list.append(stock_attribute_d)
        print("Data extraction for {} complete!".format(stock_symbol))
    concat_data = dd.concat(stock_info_list, axis=0)
    return concat_data

    print('Alpha Vantage Data Extraction Process Complete!!')


def get_quandl_data(quandl_params):  #indicators are a list of the names of external indicators
    quandl.ApiConfig.api_key = auth.apikey_quandl
    indicator_data_list = []
    for param in quandl_params:
        dict_ = getattr(params, param)
        data = quandl.get("{}/{}".format(dict_["database_code"], dict_["dataset_code"]),
                          start_date=dict_["start_date"], end_date=dict_["end_date"])
        dd_data = dd.from_pandas(data, npartitions=5)
        indicator_data_list.append(dd_data)
    concat_indicators_dd = dd.concat(indicator_data_list, axis=1)
    return concat_indicators_dd




def write_data_to_s3(df, bucket_name, file_name):
    s3 = s3fs.S3FileSystem(anon=False, key=auth.aws_access_key_id, secret=auth.aws_secret_access_key)
    with s3.open("{}/{}.csv",format(bucket_name, file_name), "w") as f:
        df.to_csv(f)
