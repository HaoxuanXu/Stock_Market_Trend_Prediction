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
    * 20 Day Exponential Moving Average (EMA) --open & close & high & low
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
### Variable Explanations 

* ##### 200 Day Exponential Moving Average
    * Exponential Moving Average is a type of moving average that places a greater 
   and signficance on the most recent data.
    * Like all moving averages, this technical indicator is used to produce buy ans sell 
   signals based on crossovers and divergences from the historical average.
    * Traders often use several different EMA days, for instance, 20-day, 30-day, 90-day,
   and 200-day moving average.
   
* ##### Moving Average Convergence / Divergence
    * Moving Average Convergence Divergence is a trend-following momentum indicator that
    shows the relationship between two moving averages of a security's price
    * Traders use the MACD to identify when bullish or bearish momentum is high in order 
    to identify entry and exit points for trades
    * MACD is used by technical traders in stocks, bonds, commodities and FX markets
    * MACD is calculated by subtracting 12-day EMA with 26-day EMA
        * *signal line is plotted with the 9-day EMA*
        * <u>*If MACD line - 9-day EMA is positive, it signals buying option; if it's negative, 
        it signals selling option* </u>
        
* ##### Stochastic Oscillator
    * A stochastic oscillator is momentum indicator comparing a particular closing price of
    a security to a range of its prices over a certain period of time
    * It is used to generate overbought and oversold trading signals, utilizing a 0-100
    bounded range of values
   


***
Index Time Series data as well as technical indicators are listed in the params.py file

auth.py, which includes the api-key, is not included in this repo