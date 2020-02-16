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
    * 10 Yr Note Futures, Continuous Contract #2 (TY2)
***
### Technical Indicator Explanations 

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
    
        CCI = (Typical Price - Simple Moving Average) / 0.015 * Mean Deviation   
        * Typical Price = asset's price on a particular day in the time period
        * Simple Moving Average = arithmetic mean of asset's price over a time period
        * Mean Deviation = mean of the absolute deviations of the asset's price over a 
        time period
        
    * The one prerequisite to calculating the CCI is determining a time interval, which 
    plays a key role in enhancing the accuracy of the CCI.
    * Traders must also adjust their CCI entry and exit thresholds based on the volatility 
    of the underlying security; for example, a ETF is traditionally less volatile than 
    an individual stock issue.
    
* ##### Aroon Indicator
    * The Aroon indicator is a technical indicator that is used to identify trend changes in
    the price of an asset, as well as the strength of that trend.
    * The indicator measures the time between highs and the time between lows over a time
    period
        * The idea is that strong up-trends will regularly see new highs, and strong down-trends
        will regularly see new lows. The indicator signals when this is happening, and when it isn't
        
    * The Aroon indicator is composed of two lines: an up line which measures the number of 
    periods since a High, and a down line which measures the number of periods since a low.
        * ***The indicator is typically applied to 25 periods of data, so the indicator is showing
        how many periods it has been since a 25-period high or low.***
    * When the Aroon Up is above the Aroon Down, it indicates bullish price behavior.
    * When the Aroon Down is above the Aroon Up, it indicates bearish price behavior.
    * **Formula for the Aroon Indicator**
        * Aroon Up = (25 - Periods Since 25 period High)*100 / 25
        * Aroon Down = (25 - Periods Since 25 period Low)*100 / 25
    * The Aroon Up and the Aroon Down lines fluctuate between zero and 100, with values close
    to 100 indicating a strong trend and values near zero indicating a weak trend. The lower the
    Aroon Up, the weaker the Up trend and stronger the down trend, and vice versa.
    * **The main assumption underlying this indicator is that a stock's price will close 
    regularly at new highs during an up trend, and regularly make lows in a down trend.**
    * Crossover can signal entry or exit points. Up crossing above Down can be a signal to buy.
        * Down crossing above Up may be a signal to sell
        
    * Limitations of the indicator:
        * The buy and sell signals may occur too late, after a substantial price movement 
        has already occurred. This happens because the indicator is looking backwards, 
        and isn't predictive in nature
        * A crossover may look good on the indicator, but it doesn't mean that the price will
        make a big move.
    
* ##### Bollinger Bands Values (BBANDS)
    * Bollinger Band is a tool used in the technical analysis. It is defined by a series of
    lines that are plotted two standard deviations--both positively and negatively--away 
    from the simple moving average (SMA) of the price of a security, but can be adjusted
    to user preferences.
    * Bollinger Bands identify a stock's high and low volatility points. While it can be
    a real challenge to forecast future prices and price cycles, volatility changes and
    cycles are relatively easy to identify.
    
    * **Formula:**\
    BBW = (TBP - BBP) / SMAC
        * BBW: Bollinger Band Width
        * TBP: Top Bollinger Band (the top 20 periods)
        * BBP: Bottom Bollinger Band (the bottom 20 periods)
        * SMAC: Simple moving average close (the middle 20 periods)
    * A squeeze is triggered when volatility reaches a six-month low and is identified 
    when Bollinger Bands reach a six-month minimum distance apart.
    
* ##### On-Balance Volume (OBV)
    * On-Balance Volume is a volume based momentum indicator that measures positive and
    negative volume flow. The idea was that volume was the driving force behind the markets, 
    and OBV was designed to project when major moves in the market would occur
    * **Formula for OBV:**
        * If today's close is greater than yesterday's close, then today's volume is added
        to yesterday's OBV, and is considered Up volume.
        * If today's close is less than yesterday's close, then today's volume is subtracted 
        from yesterday's volume and is considered Down volume.
        * If today's close is equal to yesterday's close, then today's OBV is equal to 
        yesterday's OBV.
    * OBV gives the most reliable feedback around tests of major highs and lows, making it a
    perfect tool to measure the potential for breakouts and breakdowns

  
  

***
Index Time Series data as well as technical indicators are listed in the params.py file

auth.py, which includes the api-key, is not included in this repo