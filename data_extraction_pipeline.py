# from libraries
import time
# from files
import params
import auth
import get_data_util



# I will only look at the Vanguard S&P 500 ETF
ticker_symbol = ["VOO"]

# Names of parameters to be extracted from Quandl
quandl_parameters = [a for a in dir(params) if ("_parameters" in a)]

# Begin extracting stock market data from Alpha Vantage API
print("Extracting Alpha Vantage Data...")
alpha_start_ = time.perf_counter()
alpha_vantage_data = get_data_util.get_alpha_vantage_data(ticker_symbol)
alpha_end_ = time.perf_counter() - alpha_start_
print("Extraction Complete!!! Runtime: {} seconds!".format(str(round(alpha_end_, 2))))

# Begin extracting external indicator data from Quandl API
print("Extracting Quandl data...")
quandl_start_ = time.perf_counter()
quandl_data = get_data_util.get_quandl_data(quandl_parameters)
quandl_end_ = time.perf_counter() - quandl_start_
print("Extraction Complete!!! Runtime: {} seconds!".format(str(round(quandl_end_, 2))))


# Begin merging the Alpha Vantage data and the Quandl data
print("Begin merging Alpha Vantage and Quandl Data...")
stock_market_data = alpha_vantage_data.join(quandl_data)
print("Merge Complete!!!")

# Begin writing the joined data to AWS s3
print("Begin writing data to AWS s3!!")
get_data_util.write_data_to_s3(df=stock_market_data, bucket_name=auth.bucket_name, file_name="Vanguard_S&P500_ETF_data")
print("Data writing complete!!")


# Reading in the data from aws s3
print("Start writing data to csv")
df = get_data_util.get_data_from_s3(bucket_name = auth.bucket_name,
                          file_name = "Vanguard_S&P500_ETF_data",
                          aws_key = auth.aws_access_key_id,
                          aws_secret = auth.aws_secret_access_key)

# Outputting the file as a csv file
df.to_csv("vanguard_s&p500.csv")
print("Data Extraction process complete!")