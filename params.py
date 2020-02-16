# from libraries:
import datetime as dt

# from files:
import auth

# This file documents all the parameters for index time-series as well as for technical indicators
# symbol is omitted in the current parameters and will be added later in the for loop


'''
For Stock Time-series: 
    All current companies listed in S&P 500
'''
stock_time_series_adjusted_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "outputsize": "full",
    "datatype": "csv",
    "apikey": auth.apikey_av_premium
}
'''
For External Factors (Commodity Price, Exchange Rate) --using Quandl:
    US Treasury (Treasury Yield Curve Rates)--"us_treasury_yield_parameters",
    Wiki Continuous Futures (US Dollar Index Futures, Continuous Contract)--"us_dollar_index_futures_parameters",
    Wiki Continuous Futures (30 Day Federal Funds Futures, Continuous Contract #16 (FF16))--"thirty_day_fed_fund_futures_parameters",
    Wiki Continuous Futures (Gold Futures, Continuous Contract #2 (GC2))--"gold_futures_parameters",
    Wiki Continuous Futures (E-mini Crude Oil Futures, Continuous Contract #1 (QM1) (Front Month))--"crude_oil_futures_parameters",
    Corporate Bond Yield Rates (US Corporate Bond Index Yield)--"us_corporate_bond_index_yield_parameters",
    Wiki Continuous Futures (Random Length Lumber Futures, Continuous Contract #1 (LB1) (Front Month))--"lumber_futures_parameters",
    Wiki Continuous Futures (Cotton No. 2 Futures, Continuous Contract)--"cotton_futures_parameters",
    Wiki Continuous Futures (Wheat Futures, Continuous Contract #6 (W6))--"wheat_futures_parameters",
    Wiki Continuous Futures (Coffee C Futures, Continuous Contract)--"coffee_futures_parameters"
'''

treasury_yield_curve_parameters = {
    "database_code": "USTREASURY",
    "dataset_code": "YIELD",
    "start_date": str(dt.datetime(year=dt.datetime.now().year - 20, month=dt.datetime.now().month,
                                  day=dt.datetime.now().day)),
    "end_date": str(dt.datetime.now().strftime("%Y-%m-%d"))
}


dollar_index_futures_parameters = {
    "database_code": "CHRIS",
    "dataset_code": "ICE_DX2",
    "start_date": str(dt.datetime(year=dt.datetime.now().year - 20, month=dt.datetime.now().month,
                                  day=dt.datetime.now().day)),
    "end_date": str(dt.datetime.now().strftime("%Y-%m-%d"))
}

fedfund_futures_parameters = {
    "database_code": "CHRIS",
    "dataset_code": "CME_FF16",
    "start_date": str(dt.datetime(year=dt.datetime.now().year - 20, month=dt.datetime.now().month,
                                  day=dt.datetime.now().day)),
    "end_date": str(dt.datetime.now().strftime("%Y-%m-%d"))
}

gold_futures_parameters = {
    "database_code": "CHRIS",
    "dataset_code": "CME_GC2",
    "start_date": str(dt.datetime(year=dt.datetime.now().year - 20, month=dt.datetime.now().month,
                                  day=dt.datetime.now().day)),
    "end_date": str(dt.datetime.now().strftime("%Y-%m-%d"))
}

crudeoil_futures_parameters = {
    "database_code": "CHRIS",
    "dataset_code": "CME_CL11",
    "start_date": str(dt.datetime(year=dt.datetime.now().year - 20, month=dt.datetime.now().month,
                                  day=dt.datetime.now().day)),
    "end_date": str(dt.datetime.now().strftime("%Y-%m-%d"))
}

'''
For Technical Indicators:
    200 Day Exponential Moving Average (EMA) --open & close & high & low,
    Moving Average Convergence / Divergence (MACD) --open & close & high & low,
    Stochastic Oscillator (STOCH),
    Relative Strength Index (RSI) --open & close & high & low,
    Commodity Channel Index (CCI),
    Aroon Indicator (AROON),
    Bollinger Bands Values (BBANDS) --open & close & high & low,
    On Balance Volume (OBV),
'''

sma_close_20_params = {
    "function": "SMA",
    "interval": "daily",
    "time_period": 20,
    "series_type": "close",
    "datatype":"csv",
    "apikey": auth.apikey_av_premium
}

sma_close_100_params = {
    "function": "SMA",
    "interval": "daily",
    "time_period": 100,
    "series_type": "close",
    "datatype":"csv",
    "apikey": auth.apikey_av_premium
}


macd_close_params = {
    "function": "MACD",
    "interval": "daily",
    "series_type": "close",
    "datatype":"csv",
    "apikey": auth.apikey_av_premium
}


stoch_params = {
    "function": "STOCH",
    "interval": "daily",
    "datatype":"csv",
    "apikey": auth.apikey_av_premium
}


rsi_close_params = {
    "function": "RSI",
    "interval": "daily",
    "time_period": 14,
    "series_type": "close",
    "datatype":"csv",
    "apikey": auth.apikey_av_premium
}


cci_params = {
    "function": "CCI",
    "interval": "daily",
    "time_period": 14,
    "datatype":"csv",
    "apikey": auth.apikey_av_premium
}

aroon_params = {
    "function": "AROON",
    "interval": "daily",
    "time_period": 25,
    "datatype":"csv",
    "apikey": auth.apikey_av_premium
}


bbands_close_params = {
    "function": "BBANDS",
    "interval": "daily",
    "time_period": 20,
    "series_type": "close",
    "datatype":"csv",
    "apikey": auth.apikey_av_premium
}

obv_params = {
    "function": "OBV",
    "interval": "daily",
    "datatype":"csv",
    "apikey": auth.apikey_av_premium
}


