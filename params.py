
# This file documents all the parameters for index time-series as well as for technical indicators
# symbol is omitted in the current parameters and will be added later in the for loop
import auth

'''
For Index Funds: 
    Vanguard 500 Index Fund Investor Share (VFINX),
    Vanguard Total Stock Market Index Fund (VTSMX),
    Fidelity 500 Index Fund (FXAIX),
    Schwab Total Stock Market Index Fund (SWTSX)
'''
index_params = {
    "function": "Time_Series_Daily",
    "outputsize": "full",
    "datatype": "json",
    "apikey": auth.apikey
}

'''
For Technical Indicators:
    Simple Moving Average (SMA) --daily open & daily close
'''
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

STOCH_params = {
    "function":"STOCH",
    "interval":"daily",
    "apikey":auth.apikey
}

RSI_open_params = {
    "function":"RSI",
    "interval":"daily",
    "time_period":200,
    "series_type":"open",
    "apikey":auth.apikey
}

RSI_close_params = {
    "function":"RSI",
    "interval":"daily",
    "time_period":200,
    "series_type":"close",
    "apikey":auth.apikey
}

ADX_params = {
    "function":"ADX",
    "interval":"daily",
    "time_period":200,
    "apikey":auth.apikey
}

MOM_open_params = {
    "function":"MOM",
    "interval":"daily",
    "time_period":200,
    "series_type":"open",
    "apikey":auth.apikey
}

MOM_close_params = {
    "function":"MOM",
    "interval":"daily",
    "time_period":200,
    "series_type":"close",
    "apikey":auth.apikey
}

BOP_params = {
    "function":"BOP",
    "interval":"daily",
    "apikey":auth.apikey
}

CCI_params = {
    "function":"CCI",
    "interval":"daily",
    "time_period":200,
    "apikey":auth.apikey
}

ROC_open_params = {
    "function":"ROC",
    "interval":"daily",
    "time_period":200,
    "series_type":"open",
    "apikey":auth.apikey
}

ROC_close_params = {
    "function":"ROC",
    "interval":"daily",
    "time_period":200,
    "series_type":"close",
    "apikey":auth.apikey
}

AROON_params = {
    "function":"AROON",
    "interval":"daily",
    "time_period":200,
    "apikey":auth.apikey
}

MFI_params = {
    "function":"MFI",
    "interval":"daily",
    "time_period":200,
    "apikey":auth.apikey
}

DX_params = {
    "function":"DX",
    "interval":"daily",
    "time_period":200,
    "apikey":auth.apikey
}

BBANDS_open_params = {
    "function":"BBANDS",
    "interval":"daily",
    "time_period":200,
    "series_type":"open",
    "apikey":auth.apikey
}

BBANDS_close_params = {
    "function":"BBANDS",
    "interval":"daily",
    "time_period":200,
    "series_type":"close",
    "apikey":auth.apikey
}

SAR_params = {
    "function":"SAR",
    "interval":"daily",
    "apikey":auth.apikey
}

TRANGE_params = {
    "function":"TRANGE",
    "interval":"daily",
    "apikey":auth.apikey
}

AD_params = {
    "function":"AD",
    "interval":"daily",
    "apikey":auth.apikey
}

OBV_params = {
    "function":"OBV",
    "interval":"daily",
    "apikey":auth.apikey
}

HT_TRENDLINE_open_params = {
    "function":"HT_TRENDLINE",
    "interval":"daily",
    "series_type":"open",
    "apikey":auth.apikey
}

HT_TRENDLINE_close_params = {
    "function":"HT_TRENDLINE",
    "interval":"daily",
    "series_type":"close",
    "apikey":auth.apikey
}