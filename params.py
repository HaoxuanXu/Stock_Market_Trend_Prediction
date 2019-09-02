
# This file documents all the parameters for index time-series as well as for technical indicators
# symbol is omitted in the current parameters and will be added later in the for loop
import auth

index_params = {
    "function": "Time_Series_Daily",
    "outputsize": "full",
    "datatype": "json",
    "apikey": auth.apikey
}

SMA_open_params = {
    "function":"SMA",
    "interval":"daily",
    "time_period":200,
    "series_type":"open",
    "apikey":auth.apikey
}

SMA_close_params = {
    "function":"SMA",
    "interval":"daily",
    "time_period":200,
    "series_type":"close",
    "apikey":auth.apikey
}

EMA_open_params = {
    "function":"EMA",
    "interval":"daily",
    "time_period":200,
    "series_type":"open",
    "apikey":auth.apikey
}

EMA_close_params = {
    "function":"EMA",
    "interval":"daily",
    "time_period":200,
    "series_type":"close",
    "apikey":auth.apikey
}

MACD_open_params = {
    "function":"MACD",
    "interval":"daily",
    "series_type":"open",
    "apikey":auth.apikey
}

MACD_close_params = {
    "function":"MACD",
    "interval":"daily",
    "series_type":"close",
    "apikey":auth.apikey
}