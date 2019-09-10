# from libraries
import pandas as pd
import dask.dataframe as dd
# from files
import params
import auth
import get_data_util
import get_sp500_util as sp500

temp_file_folder = "C:/Users/John Xu/Desktop/Stock_Market_Trend_Prediction/temp_file/"
# list of S&P 500 companies tickers
ticker_list = sp500.get_sp_500(url=sp500.url, headers=auth.user_agent)
# Names of parameters to be extracted from Quandl
quandl_parameters = [a for a in dir(params) if ("_parameters" in a)]


alpha_vantage_data = get_data_util.get_alpha_vantage_data(ticker_list[:2])
quandl_data = get_data_util.get_quandl_data(quandl_parameters[:3])

#alpha_vantage_data.to_csv(temp_file_folder+"temp_alpha.csv")
#quandl_data.to_csv(temp_file_folder+"temp_quandl.csv")

stock_market_data = dd.merge(alpha_vantage_data, quandl_data)
#stock_market_data = alpha_vantage_data.join(quandl_data, how="outer")
#stock_market_data_pickle = stock_market_data.copy()
#stock_market_data_pickle.to_pickle(temp_file_folder+"temp_data_file.pkl")
stock_market_data.to_csv(temp_file_folder+"temp_data_file.csv")

#get_data_util.write_data_to_s3(df=stock_market_data, bucket_name=auth.bucket_name, file_name="stock_market_data")