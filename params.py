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
    Wiki Continuous Futures (Soybean Futures, Continuous Contract #2 (S2))--"us_soybean_futures_parameters",
    Wiki Continuous Futures (Corn Futures, Continuous Contract #2 (EMA2))--"us_corn_futures_parameters",
    US Treasury (Treasury Yield Curve Rates)--"us_treasury_yield_parameters",
    Wiki Continuous Futures (US Dollar Index Futures, Continuous Contract)--"us_dollar_index_futures_parameters",
    Wiki Continuous Futures (30 Day Federal Funds Futures, Continuous Contract #16 (FF16))--"thirty_day_fed_fund_futures_parameters",
    Wiki Continuous Futures (S&P 500 Futures, Continuous Contract #1 (SP1) (Front Month))--"sp500_futures_parameters",
    Wiki Continuous Futures (Gold Futures, Continuous Contract #2 (GC2))--"gold_futures_parameters",
    Wiki Continuous Futures (E-mini Crude Oil Futures, Continuous Contract #1 (QM1) (Front Month))--"crude_oil_futures_parameters",
    Corporate Bond Yield Rates (US Corporate Bond Index Yield)--"us_corporate_bond_index_yield_parameters",
    Wiki Continuous Futures (Random Length Lumber Futures, Continuous Contract #1 (LB1) (Front Month))--"lumber_futures_parameters",
    Wiki Continuous Futures (Cotton No. 2 Futures, Continuous Contract)--"cotton_futures_parameters",
    Wiki Continuous Futures (Wheat Futures, Continuous Contract #6 (W6))--"wheat_futures_parameters",
    Wiki Continuous Futures (Coffee C Futures, Continuous Contract)--"coffee_futures_parameters"
'''

us_soybean_futures_parameters = {
    "database_code": "CHRIS",
    "dataset_code": "CME_S2",
    "start_date": str(dt.datetime(year=dt.datetime.now().year - 20, month=dt.datetime.now().month,
                                  day=dt.datetime.now().day)),
    "end_date": str(dt.datetime.now().strftime("%Y-%m-%d"))
}

us_corn_futures_parameters = {
    "database_code": "CHRIS",
    "dataset_code": "LIFFE_EMA2",
    "start_date": str(dt.datetime(year=dt.datetime.now().year - 20, month=dt.datetime.now().month,
                                  day=dt.datetime.now().day)),
    "end_date": str(dt.datetime.now().strftime("%Y-%m-%d"))
}

us_treasury_yield_parameters = {
    "database_code": "USTREASURY",
    "dataset_code": "REALYIELD",
    "start_date": str(dt.datetime(year=dt.datetime.now().year - 20, month=dt.datetime.now().month,
                                  day=dt.datetime.now().day)),
    "end_date": str(dt.datetime.now().strftime("%Y-%m-%d"))
}

us_dollar_index_futures_parameters = {
    "database_code": "CHRIS",
    "dataset_code": "ICE_DX2",
    "start_date": str(dt.datetime(year=dt.datetime.now().year - 20, month=dt.datetime.now().month,
                                  day=dt.datetime.now().day)),
    "end_date": str(dt.datetime.now().strftime("%Y-%m-%d"))
}

thirty_day_fed_fund_futures_parameters = {
    "database_code": "CHRIS",
    "dataset_code": "CME_FF16",
    "start_date": str(dt.datetime(year=dt.datetime.now().year - 20, month=dt.datetime.now().month,
                                  day=dt.datetime.now().day)),
    "end_date": str(dt.datetime.now().strftime("%Y-%m-%d"))
}

sp500_futures_parameters = {
    "database_code": "CHRIS",
    "dataset_code": "CME_SP1",
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

crude_oil_futures_parameters = {
    "database_code": "CHRIS",
    "dataset_code": "CME_QM1",
    "start_date": str(dt.datetime(year=dt.datetime.now().year - 20, month=dt.datetime.now().month,
                                  day=dt.datetime.now().day)),
    "end_date": str(dt.datetime.now().strftime("%Y-%m-%d"))
}

us_corporate_bond_index_yield_parameters = {
    "database_code": "ML",
    "dataset_code": "USEY",
    "start_date": str(dt.datetime(year=dt.datetime.now().year - 20, month=dt.datetime.now().month,
                                  day=dt.datetime.now().day)),
    "end_date": str(dt.datetime.now().strftime("%Y-%m-%d"))
}

lumber_futures_parameters = {
    "database_code": "CHRIS",
    "dataset_code": "CME_LB1",
    "start_date": str(dt.datetime(year=dt.datetime.now().year - 20, month=dt.datetime.now().month,
                                  day=dt.datetime.now().day)),
    "end_date": str(dt.datetime.now().strftime("%Y-%m-%d"))
}

cotton_futures_parameters = {
    "database_code": "CHRIS",
    "dataset_code": "ICE_CT3",
    "start_date": str(dt.datetime(year=dt.datetime.now().year - 20, month=dt.datetime.now().month,
                                  day=dt.datetime.now().day)),
    "end_date": str(dt.datetime.now().strftime("%Y-%m-%d"))
}

wheat_futures_parameters = {
    "database_code": "CHRIS",
    "dataset_code": "CME_W6",
    "start_date": str(dt.datetime(year=dt.datetime.now().year - 20, month=dt.datetime.now().month,
                                  day=dt.datetime.now().day)),
    "end_date": str(dt.datetime.now().strftime("%Y-%m-%d"))
}

coffee_futures_parameters = {
    "database_code": "CHRIS",
    "dataset_code": "ICE_KC5",
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
    Chaikin A/D Line Values (AD),
    On Balance Volume (OBV),
'''

ema_open_params_200 = {
    "function": "EMA",
    "interval": "daily",
    "time_period": 200,
    "series_type": "open",
    "datatype":"csv",
    "apikey": auth.apikey_av_premium
}

ema_close_params = {
    "function": "EMA",
    "interval": "daily",
    "time_period": 200,
    "series_type": "close",
    "datatype":"csv",
    "apikey": auth.apikey_av_premium
}

ema_high_params = {
    "function": "EMA",
    "interval": "daily",
    "time_period": 200,
    "series_type": "close",
    "datatype":"csv",
    "apikey": auth.apikey_av_premium
}

ema_low_params = {
    "function": "EMA",
    "interval": "daily",
    "time_period": 200,
    "series_type": "low",
    "datatype":"csv",
    "apikey": auth.apikey_av_premium
}

macd_open_params = {
    "function": "MACD",
    "interval": "daily",
    "series_type": "open",
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

macd_high_params = {
    "function": "MACD",
    "interval": "daily",
    "series_type": "high",
    "datatype":"csv",
    "apikey": auth.apikey_av_premium
}

macd_low_params = {
    "function": "MACD",
    "interval": "daily",
    "series_type": "low",
    "datatype":"csv",
    "apikey": auth.apikey_av_premium
}

stoch_params = {
    "function": "STOCH",
    "interval": "daily",
    "datatype":"csv",
    "apikey": auth.apikey_av_premium
}

rsi_open_params = {
    "function": "RSI",
    "interval": "daily",
    "time_period": 14,
    "series_type": "open",
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

rsi_high_params = {
    "function": "RSI",
    "interval": "daily",
    "time_period": 14,
    "series_type": "high",
    "datatype":"csv",
    "apikey": auth.apikey_av_premium
}

rsi_low_params = {
    "function": "RSI",
    "interval": "daily",
    "time_period": 14,
    "series_type": "low",
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
    "time_period": 14,
    "datatype":"csv",
    "apikey": auth.apikey_av_premium
}

bbands_open_params = {
    "function": "BBANDS",
    "interval": "daily",
    "time_period": 20,
    "series_type": "open",
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

bbands_high_params = {
    "function": "BBANDS",
    "interval": "daily",
    "time_period": 20,
    "series_type": "high",
    "datatype":"csv",
    "apikey": auth.apikey_av_premium
}

bbands_low_params = {
    "function": "BBANDS",
    "interval": "daily",
    "time_period": 20,
    "series_type": "low",
    "datatype":"csv",
    "apikey": auth.apikey_av_premium
}

ad_params = {
    "function": "AD",
    "interval": "daily",
    "datatype":"csv",
    "apikey": auth.apikey_av_premium
}

obv_params = {
    "function": "OBV",
    "interval": "daily",
    "datatype":"csv",
    "apikey": auth.apikey_av_premium
}


