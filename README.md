# Stock_Market_Trend_Prediction
Using API from Alpha Vantage and Quandl to train and test multiple machine learning algorithms for Stock_Market movement prediction

* In order to make this work, you should have downloaded quandl python package:
    * ##### pip install quandl

* You need to include the API keys for both Alpha Vantage and Quandl to be able to access the data from them

***
#### This project extracts daily open, close, high, low, and adjusted values from Vanguard S&P 500 ETF history

It includes multiple technical indicators and external pricing information as features
* ##### Technical Indicators
    
    * 200 Day Exponential Moving Average (EMA) --open & close & high & low
    * 200 Day Simple Moving Average (SMA) --open & close & high & low
    * Moving Average Convergence / Divergence (MACD) --open & close & high & low
    * Stochastic Oscillator (STOCH)
    * Relative Strength Index (RSI) --open & close & high & low
    * Commodity Channel Index (CCI)
    * Aroon Indicator (AROON)
    * Bollinger Bands Values (BBANDS) --open & close & high & low
    * Chaikin A/D Line Values (AD)
    * On Balance Volume (OBV)
    

* ##### External Factors (from Wiki Continuous Futures)
    * US Treasury (Treasury Yield Curve Rates) --"us_treasury_yield_parameters"
    * US Dollar Index Futures, Continuous Contract 
    * 30 Day Federal Funds Futures, Continuous Contract #16 (FF16) 
    * Gold Futures, Continuous Contract #2 (GC2)
    * E-mini Crude Oil Futures, Continuous Contract #1 (QM1) (Front Month)
    * US Corporate Bond Index Yield
    * 10 Yr Note Futures, Continuous Contract #2 (TY2)


***
Index Time Series data as well as technical indicators are listed in the params.py file

auth.py, which includes the api-key, is not included in this repo