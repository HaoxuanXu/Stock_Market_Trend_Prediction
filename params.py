# from libraries:
import datetime as dt

# from files:
import auth

# This file documents all the parameters for index time-series as well as for technical indicators
# symbol is omitted in the current parameters and will be added later in the for loop


'''
For Index Funds: 
    Vanguard 500 Index Fund Investor Share (VFINX),
    Vanguard Total Stock Market Index Fund (VTSMX),
    Fidelity 500 Index Fund (FXAIX),
    Schwab Total Stock Market Index Fund (SWTSX)
'''
index_fund_params = {
    "function": "Time_Series_Daily",
    "outputsize": "full",
    "datatype": "json",
    "apikey": auth.apikey_av
}
'''
For External Factors (Commodity Price, Exchange Rate) --using Quandl:
    Global Petroleum Prices (Change in fuel prices--USA)--"us_petro_params",
    Wiki Continuous Futures (Minneapolis NSI National Soybean Futures, Continuous Contract #1 (IS1) (Front Month))--"us_soybean_futures_params",
    Wiki Continuous Futures (Minneapolis NCI National Corn Futures, Continuous Contract #1 (IC1) (Front Month))--"us_corn_futures_params"
'''
us_petro_params = {
    "database_code": "GPP",
    "dataset_code": "CFP_USA",
    "start_date": str(dt.datetime(year=dt.datetime.now().year - 20, month=dt.datetime.now().month,
                                  day=dt.datetime.now().day)),
    "end_date": str(dt.datetime.now().strftime("%Y-%m-%d"))
}

us_soybean_futures_params = {
    "database_code": "CHRIS",
    "dataset_code": "MGEX_IS1",
    "start_date": str(dt.datetime(year=dt.datetime.now().year - 20, month=dt.datetime.now().month,
                                  day=dt.datetime.now().day)),
    "end_date": str(dt.datetime.now().strftime("%Y-%m-%d"))
}

us_corn_futures_params = {
    "database_code": "CHRIS",
    "dataset_code": "MGEX_IC1",
    "start_date": str(dt.datetime(year=dt.datetime.now().year - 20, month=dt.datetime.now().month,
                                  day=dt.datetime.now().day)),
    "end_date": str(dt.datetime.now().strftime("%Y-%m-%d"))
}
'''
For Technical Indicators:
    Simple Moving Average (SMA) --daily open & daily close,
    Exponential Moving Average (EMA) --daily open & daily close,
    Moving Average Convergence / Divergence (MACD) --daily open & daily close,
    Stochastic Oscillator (STOCH),
    Relative Strength Index (RSI) --daily open & daily close,
    Average Directional Movement Index (ADX),
    Momentum (MOM) --daily open & daily close,
    Balance of Power (BOP),
    Commodity Channel Index (CCI),
    Rate of Change (ROC) --daily open & daily close,
    Aroon Indicator (AROON),
    Money Flow Index (MFI),
    Directional Movement Index (DX),
    Bollinger Bands Values (BBANDS) --daily open & daily close
    Parabolic SAR Values (SAR),
    True Range Values (TRANGE),
    Chaikin A/D Line Values (AD),
    On Balance Volume (OBV),
    Hilbert Transform, Instantaneous Trendline (HT_TRENDLINE) --daily open & daily close
'''
sma_open_params = {
    "function": "SMA",
    "interval": "daily",
    "time_period": 200,
    "series_type": "open",
    "apikey": auth.apikey_av
}

sma_close_params = {
    "function": "SMA",
    "interval": "daily",
    "time_period": 200,
    "series_type": "close",
    "apikey": auth.apikey_av
}

ema_open_params = {
    "function": "EMA",
    "interval": "daily",
    "time_period": 200,
    "series_type": "open",
    "apikey": auth.apikey_av
}

ema_close_params = {
    "function": "EMA",
    "interval": "daily",
    "time_period": 200,
    "series_type": "close",
    "apikey": auth.apikey_av
}

macd_open_params = {
    "function": "MACD",
    "interval": "daily",
    "series_type": "open",
    "apikey": auth.apikey_av
}

macd_close_params = {
    "function": "MACD",
    "interval": "daily",
    "series_type": "close",
    "apikey": auth.apikey_av
}

stoch_params = {
    "function": "STOCH",
    "interval": "daily",
    "apikey": auth.apikey_av
}

rsi_open_params = {
    "function": "RSI",
    "interval": "daily",
    "time_period": 200,
    "series_type": "open",
    "apikey": auth.apikey_av
}

rsi_close_params = {
    "function": "RSI",
    "interval": "daily",
    "time_period": 200,
    "series_type": "close",
    "apikey": auth.apikey_av
}

adx_params = {
    "function": "ADX",
    "interval": "daily",
    "time_period": 200,
    "apikey": auth.apikey_av
}

mom_open_params = {
    "function": "MOM",
    "interval": "daily",
    "time_period": 200,
    "series_type": "open",
    "apikey": auth.apikey_av
}

mom_close_params = {
    "function": "MOM",
    "interval": "daily",
    "time_period": 200,
    "series_type": "close",
    "apikey": auth.apikey_av
}

bop_params = {
    "function": "BOP",
    "interval": "daily",
    "apikey": auth.apikey_av
}

cci_params = {
    "function": "CCI",
    "interval": "daily",
    "time_period": 200,
    "apikey": auth.apikey_av
}

roc_open_params = {
    "function": "ROC",
    "interval": "daily",
    "time_period": 200,
    "series_type": "open",
    "apikey": auth.apikey_av
}

roc_close_params = {
    "function": "ROC",
    "interval": "daily",
    "time_period": 200,
    "series_type": "close",
    "apikey": auth.apikey_av
}

aroon_params = {
    "function": "AROON",
    "interval": "daily",
    "time_period": 200,
    "apikey": auth.apikey_av
}

mfi_params = {
    "function": "MFI",
    "interval": "daily",
    "time_period": 200,
    "apikey": auth.apikey_av
}

dx_params = {
    "function": "DX",
    "interval": "daily",
    "time_period": 200,
    "apikey": auth.apikey_av
}

bbands_open_params = {
    "function": "BBANDS",
    "interval": "daily",
    "time_period": 200,
    "series_type": "open",
    "apikey": auth.apikey_av
}

bbands_close_params = {
    "function": "BBANDS",
    "interval": "daily",
    "time_period": 200,
    "series_type": "close",
    "apikey": auth.apikey_av
}

sar_params = {
    "function": "SAR",
    "interval": "daily",
    "apikey": auth.apikey_av
}

trange_params = {
    "function": "TRANGE",
    "interval": "daily",
    "apikey": auth.apikey_av
}

ad_params = {
    "function": "AD",
    "interval": "daily",
    "apikey": auth.apikey_av
}

obv_params = {
    "function": "OBV",
    "interval": "daily",
    "apikey": auth.apikey_av
}

ht_trendline_open_params = {
    "function": "HT_TRENDLINE",
    "interval": "daily",
    "series_type": "open",
    "apikey": auth.apikey_av
}

ht_trendline_close_params = {
    "function": "HT_TRENDLINE",
    "interval": "daily",
    "series_type": "close",
    "apikey": auth.apikey_av
}
