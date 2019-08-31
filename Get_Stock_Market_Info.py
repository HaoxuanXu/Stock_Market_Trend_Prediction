#from libraries
import requests


#from files:
import auth

# url_base:
alpha-vantage-base = "https://www.alphavantage.co"

#initialization:
params = {
    "function":"Time_Series_Daily_Adjusted",
    "symbol":"VOO",
    "outputsize":"full"
}
