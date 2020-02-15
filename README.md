# Stock_Market_Trend_Prediction
Using API from Alpha Vantage and Quandl to train and test multiple machine learning algorithms for Stock_Market movement prediction

* In order to make this work, you should have downloaded quandl python package:
    * ##### pip install quandl

* You need to include the API keys for both Alpha Vantage and Quandl to be able to access the data from them

***
#### This project extracts daily open, close, high, low, and adjusted values from Vanguard S&P 500 ETF history

It includes multiple technical indicators and external pricing information as features
* ##### Technical Indicators
    
    * 200 Day Exponential Moving Average (EMA-200) 
    * 20 Day Exponential Moving Average (EMA-20) 
    * 9 Day Exponential Moving Average (EMA-9) -- ***used as signal for MACD***
    * Moving Average Convergence / Divergence (MACD) 
    * Stochastic Oscillator (STOCH)
    * Relative Strength Index (RSI) 
    * Commodity Channel Index (CCI)
    * Aroon Indicator (AROON)
    * Bollinger Bands Values (BBANDS) 
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
        
* ##### Stochastic Oscillator (similar to min-max scaling)
    * A stochastic oscillator is momentum indicator comparing a particular closing price of
    a security to a range of its prices over a certain period of time
    * It is used to generate overbought and oversold trading signals, utilizing a 0-100
    bounded range of values
    * Formula: 
        * %K = (C - L14) * 100 / (H14 - L14)
            * C: The most recent closing price
            * L14: The lowest price traded of the 14 previous trading sessions
            * H14: The highest price traded during the same 14-day period
            * %K: The current value of the stochastic indicator
       
    * Traditionally, readings over 80 are considered in the overbought range, and readings 
    under 20 are considered oversold. However, these are not always indicative of impending
    reversal; very strong trends can maintain overbought or oversold conditions for an extended
    period.
        * Traders should look to changes in the stochastic oscillator for clues about future 
        trend shifts
   
* ##### Relative Strength Index (RSI)
    * Relative Strength Index describes a momentum indicator that measures the magnitude 
    of recent price changes in order to evaluate overbought or oversold conditions in the 
    price of a stock or other assets.
    * The RSI is displayed as an oscillator, which is a line graph that moves between
    two extremes. Its readings can range from 0 to 100.
    * Traditional interpretation and usage of the RSI dictates that values of 70 or above
    suggest that a security is becoming overbought or overvalued and may be primed for a
    trend reversal or corrective price pullback. An RSI reading of 30 or below indicates an
    oversold or undervalued condition.
    * During an uptrend, the RSI tends to stay above 30 and should frequently hit 70. During
    a downtrend, it is rare to see the RSI exceed 70, and the indicator frequently hits 30
    or under.
 
* ##### Commodity Channel Index (CCI)
    * Like most oscillators, the CCI was developed to determine overbought and oversold levels. 
    The CCI does this by measuring the relationship between price and a moving average, or
    more specifically, normal deviations from that average   
  

***
Index Time Series data as well as technical indicators are listed in the params.py file

auth.py, which includes the api-key, is not included in this repo