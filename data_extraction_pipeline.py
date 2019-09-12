# from libraries
import pandas as pd
import dask.dataframe as dd
# from files
import params
import auth
import get_data_util
import get_dow_jones_util as dj


# list of Dow Jones companies tickers
ticker_list = dj.get_dow_jones(url=dj.url, headers=auth.user_agent)

# Names of parameters to be extracted from Quandl
quandl_parameters = [a for a in dir(params) if ("_parameters" in a)]


alpha_vantage_data = get_data_util.get_alpha_vantage_data(ticker_list)
quandl_data = get_data_util.get_quandl_data(quandl_parameters)



print("Begin merging Alpha Vantage and Quandl Data...")
stock_market_data = alpha_vantage_data.join(quandl_data)
print("Merge Complete!!!")


print("Begin writing data to AWS s3!!")
get_data_util.write_data_to_s3(df=stock_market_data, bucket_name=auth.bucket_name, file_name="dow_jones_stock_market_data")
print("Data writing complete!!")