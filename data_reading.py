# from files
import get_data_util
import auth
import pandas as pd

# Reading in the data from aws s3
df = get_data_util.get_data_from_s3(bucket_name = auth.bucket_name,
                          file_name = "Vanguard_S&P500_ETF_data",
                          aws_key = auth.aws_access_key_id,
                          aws_secret = auth.aws_secret_access_key)

# Outputting the file as a csv file
df.to_csv("vanguard_s&p500.csv")
