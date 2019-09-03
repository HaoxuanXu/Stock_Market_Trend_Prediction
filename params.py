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
    Global Petroleum Prices (Change in fuel prices--USA)--"US_Petro_params",
    Wiki Continuous Futures (Minneapolis NSI National Soybean Futures, Continuous Contract #1 (IS1) (Front Month))--"US_Soybean_Futures_params",
    Wiki Continuous Futures (Minneapolis NCI National Corn Futures, Continuous Contract #1 (IC1) (Front Month))--"US_Corn_Futures_params"
'''
US_Petro_params = {
    "database_code": "GPP",
    "dataset_code": "CFP_USA",
    "start_date": str(dt.datetime(year=dt.datetime.now().year - 20, month=dt.datetime.now().month,
                                  day=dt.datetime.now().day)),
    "end_date": str(dt.datetime.now().strftime("%Y-%m-%d"))
}

US_Soybean_Futures_params = {
    "database_code": "CHRIS",
    "dataset_code": "MGEX_IS1",
    "start_date": str(dt.datetime(year=dt.datetime.now().year - 20, month=dt.datetime.now().month,
                                  day=dt.datetime.now().day)),
    "end_date": str(dt.datetime.now().strftime("%Y-%m-%d"))
}

US_Corn_Futures_params = {
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
SMA_open_params = {
    "function": "SMA",
    "interval": "daily",
    "time_period": 200,
    "series_type": "open",
    "apikey": auth.apikey_av
}

SMA_close_params = {
    "function": "SMA",
    "interval": "daily",
    "time_period": 200,
    "series_type": "close",
    "apikey": auth.apikey_av
}

EMA_open_params = {
    "function": "EMA",
    "interval": "daily",
    "time_period": 200,
    "series_type": "open",
    "apikey": auth.apikey_av
}

EMA_close_params = {
    "function": "EMA",
    "interval": "daily",
    "time_period": 200,
    "series_type": "close",
    "apikey": auth.apikey_av
}

MACD_open_params = {
    "function": "MACD",
    "interval": "daily",
    "series_type": "open",
    "apikey": auth.apikey_av
}

MACD_close_params = {
    "function": "MACD",
    "interval": "daily",
    "series_type": "close",
    "apikey": auth.apikey_av
}

STOCH_params = {
    "function": "STOCH",
    "interval": "daily",
    "apikey": auth.apikey_av
}

RSI_open_params = {
    "function": "RSI",
    "interval": "daily",
    "time_period": 200,
    "series_type": "open",
    "apikey": auth.apikey_av
}

RSI_close_params = {
    "function": "RSI",
    "interval": "daily",
    "time_period": 200,
    "series_type": "close",
    "apikey": auth.apikey_av
}

ADX_params = {
    "function": "ADX",
    "interval": "daily",
    "time_period": 200,
    "apikey": auth.apikey_av
}

MOM_open_params = {
    "function": "MOM",
    "interval": "daily",
    "time_period": 200,
    "series_type": "open",
    "apikey": auth.apikey_av
}

MOM_close_params = {
    "function": "MOM",
    "interval": "daily",
    "time_period": 200,
    "series_type": "close",
    "apikey": auth.apikey_av
}

BOP_params = {
    "function": "BOP",
    "interval": "daily",
    "apikey": auth.apikey_av
}

CCI_params = {
    "function": "CCI",
    "interval": "daily",
    "time_period": 200,
    "apikey": auth.apikey_av
}

ROC_open_params = {
    "function": "ROC",
    "interval": "daily",
    "time_period": 200,
    "series_type": "open",
    "apikey": auth.apikey_av
}

ROC_close_params = {
    "function": "ROC",
    "interval": "daily",
    "time_period": 200,
    "series_type": "close",
    "apikey": auth.apikey_av
}

AROON_params = {
    "function": "AROON",
    "interval": "daily",
    "time_period": 200,
    "apikey": auth.apikey_av
}

MFI_params = {
    "function": "MFI",
    "interval": "daily",
    "time_period": 200,
    "apikey": auth.apikey_av
}

DX_params = {
    "function": "DX",
    "interval": "daily",
    "time_period": 200,
    "apikey": auth.apikey_av
}

BBANDS_open_params = {
    "function": "BBANDS",
    "interval": "daily",
    "time_period": 200,
    "series_type": "open",
    "apikey": auth.apikey_av
}

BBANDS_close_params = {
    "function": "BBANDS",
    "interval": "daily",
    "time_period": 200,
    "series_type": "close",
    "apikey": auth.apikey_av
}

SAR_params = {
    "function": "SAR",
    "interval": "daily",
    "apikey": auth.apikey_av
}

TRANGE_params = {
    "function": "TRANGE",
    "interval": "daily",
    "apikey": auth.apikey_av
}

AD_params = {
    "function": "AD",
    "interval": "daily",
    "apikey": auth.apikey_av
}

OBV_params = {
    "function": "OBV",
    "interval": "daily",
    "apikey": auth.apikey_av
}

HT_TRENDLINE_open_params = {
    "function": "HT_TRENDLINE",
    "interval": "daily",
    "series_type": "open",
    "apikey": auth.apikey_av
}

HT_TRENDLINE_close_params = {
    "function": "HT_TRENDLINE",
    "interval": "daily",
    "series_type": "close",
    "apikey": auth.apikey_av
}
