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
stock_time_series_params = {
    "function": "Time_Series_Daily",
    "outputsize": "full",
    "datatype": "csv",
    "apikey": auth.apikey_av
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
    "datatype":"csv",
    "apikey": auth.apikey_av
}

sma_close_params = {
    "function": "SMA",
    "interval": "daily",
    "time_period": 200,
    "series_type": "close",
    "datatype":"csv",
    "apikey": auth.apikey_av
}

ema_open_params = {
    "function": "EMA",
    "interval": "daily",
    "time_period": 200,
    "series_type": "open",
    "datatype":"csv",
    "apikey": auth.apikey_av
}

ema_close_params = {
    "function": "EMA",
    "interval": "daily",
    "time_period": 200,
    "series_type": "close",
    "datatype":"csv",
    "apikey": auth.apikey_av
}

macd_open_params = {
    "function": "MACD",
    "interval": "daily",
    "series_type": "open",
    "datatype":"csv",
    "apikey": auth.apikey_av
}

macd_close_params = {
    "function": "MACD",
    "interval": "daily",
    "series_type": "close",
    "datatype":"csv",
    "apikey": auth.apikey_av
}

stoch_params = {
    "function": "STOCH",
    "interval": "daily",
    "datatype":"csv",
    "apikey": auth.apikey_av
}

rsi_open_params = {
    "function": "RSI",
    "interval": "daily",
    "time_period": 200,
    "series_type": "open",
    "datatype":"csv",
    "apikey": auth.apikey_av
}

rsi_close_params = {
    "function": "RSI",
    "interval": "daily",
    "time_period": 200,
    "series_type": "close",
    "datatype":"csv",
    "apikey": auth.apikey_av
}

adx_params = {
    "function": "ADX",
    "interval": "daily",
    "time_period": 200,
    "datatype":"csv",
    "apikey": auth.apikey_av
}

mom_open_params = {
    "function": "MOM",
    "interval": "daily",
    "time_period": 200,
    "series_type": "open",
    "datatype":"csv",
    "apikey": auth.apikey_av
}

mom_close_params = {
    "function": "MOM",
    "interval": "daily",
    "time_period": 200,
    "series_type": "close",
    "datatype":"csv",
    "apikey": auth.apikey_av
}

bop_params = {
    "function": "BOP",
    "interval": "daily",
    "datatype":"csv",
    "apikey": auth.apikey_av
}

cci_params = {
    "function": "CCI",
    "interval": "daily",
    "time_period": 200,
    "datatype":"csv",
    "apikey": auth.apikey_av
}

roc_open_params = {
    "function": "ROC",
    "interval": "daily",
    "time_period": 200,
    "series_type": "open",
    "datatype":"csv",
    "apikey": auth.apikey_av
}

roc_close_params = {
    "function": "ROC",
    "interval": "daily",
    "time_period": 200,
    "series_type": "close",
    "datatype":"csv",
    "apikey": auth.apikey_av
}

aroon_params = {
    "function": "AROON",
    "interval": "daily",
    "time_period": 200,
    "datatype":"csv",
    "apikey": auth.apikey_av
}

mfi_params = {
    "function": "MFI",
    "interval": "daily",
    "time_period": 200,
    "datatype":"csv",
    "apikey": auth.apikey_av
}

dx_params = {
    "function": "DX",
    "interval": "daily",
    "time_period": 200,
    "datatype":"csv",
    "apikey": auth.apikey_av
}

bbands_open_params = {
    "function": "BBANDS",
    "interval": "daily",
    "time_period": 200,
    "series_type": "open",
    "datatype":"csv",
    "apikey": auth.apikey_av
}

bbands_close_params = {
    "function": "BBANDS",
    "interval": "daily",
    "time_period": 200,
    "series_type": "close",
    "datatype":"csv",
    "apikey": auth.apikey_av
}

sar_params = {
    "function": "SAR",
    "interval": "daily",
    "datatype":"csv",
    "apikey": auth.apikey_av
}

trange_params = {
    "function": "TRANGE",
    "interval": "daily",
    "datatype":"csv",
    "apikey": auth.apikey_av
}

ad_params = {
    "function": "AD",
    "interval": "daily",
    "datatype":"csv",
    "apikey": auth.apikey_av
}

obv_params = {
    "function": "OBV",
    "interval": "daily",
    "datatype":"csv",
    "apikey": auth.apikey_av
}

ht_trendline_open_params = {
    "function": "HT_TRENDLINE",
    "interval": "daily",
    "series_type": "open",
    "datatype":"csv",
    "apikey": auth.apikey_av
}

ht_trendline_close_params = {
    "function": "HT_TRENDLINE",
    "interval": "daily",
    "series_type": "close",
    "datatype":"csv",
    "apikey": auth.apikey_av
}
