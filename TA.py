from talib.abstract import *
import talib as ta 
#from talib import *
#import talib.abstract as ta 
import pandas as pd
import numpy as np

df = pd.read_csv('BTC-USD.csv')
#print(df.head)
#import talib
df = pd.DataFrame(data = df, dtype=np.int64)
#df_ta.apply(lambda c: talib.RSI(c, timeperiod = 14))
#print(talib.get_functions())
#print( talib.get_function_groups())
print(df.head())
def MathTransformFunctions(df):
    close=df['close']
    #print(close)
    #ACOS - Vector Trigonometric ACos
    df['ACOS'] = ta.ACOS(close)
    #ASIN - Vector Trigonometric ASin
    df['ASIN'] = ta.ASIN(close)
    #ATAN - Vector Trigonometric ATan
    df['ATAN'] = ta.ATAN(close)
    #CEIL - Vector Ceil
    df['CEIL'] = ta.CEIL(close)
    #COS - Vector Trigonometric Cos
    df['COS'] = ta.COS(close)
    #COSH - Vector Trigonometric Cosh
    df['COSH'] = ta.COSH(close)
    #EXP - Vector Arithmetic Exp
    df['EXP'] = ta.EXP(close)
    #FLOOR - Vector Floor
    df['FLOOR'] = ta.FLOOR(close)
    #LN - Vector Log Natural
    df['LN'] = ta.LN(close)
    #LOG10 - Vector Log10
    df['LOG10'] = ta.LOG10(close)
    #SIN - Vector Trigonometric Sin
    df['SIN'] = ta.SIN(close)
    #SINH - Vector Trigonometric Sinh
    df['SINH'] = ta.SINH(close)
    #SQRT - Vector Square Root
    df['SQRT'] = ta.SQRT(close)
    #TAN - Vector Trigonometric Tan
    df['TAN'] = ta.TAN(close)
    #TANH - Vector Trigonometric Tanh
    df['TANH'] = ta.TANH(close)
    return df
def PriceTransformFunctions(df):
    close=df['close']
    opens=df['open']
    high=df['high']
    low=df['low']
    #AVGPRICE - Average Price
    df['AVGPRICE'] = ta.AVGPRICE(opens, high, low, close)
    #Learn more about the Average Price at tadoc.org.

    #MEDPRICE - Median Price
    df['MEDPRICE'] = ta.MEDPRICE(high, low)
    #Learn more about the Median Price at tadoc.org.

    #TYPPRICE - Typical Price
    df['MEDPRICE'] = ta.TYPPRICE(high, low, close)
    #Learn more about the Typical Price at tadoc.org.

    #WCLPRICE - Weighted Close Price
    df['WCLPRICE'] = ta.WCLPRICE(high, low, close)
    return df


def StatisticFunctions(df):
    close=df['close']
    opens=df['open']
    high=df['high']
    low=df['low']
    #BETA - Beta
    df['BETA'] = ta.BETA(high, low, timeperiod=5)
    #Learn more about the Beta at tadoc.org.

    #CORREL - Pearson's Correlation Coefficient (r)
    df['CORREL'] = ta.CORREL(high, low, timeperiod=30)
    #Learn more about the Pearson's Correlation Coefficient (r) at tadoc.org.

    #LINEARREG - Linear Regression
    df['LINEARREG'] = ta.LINEARREG(close, timeperiod=14)
    #Learn more about the Linear Regression at tadoc.org.

    #LINEARREG_ANGLE - Linear Regression Angle
    df['LINEARREG_ANGLE'] = ta.LINEARREG_ANGLE(close, timeperiod=14)
    #Learn more about the Linear Regression Angle at tadoc.org.

    #LINEARREG_INTERCEPT - Linear Regression Intercept
    df['LINEARREG_INTERCEPT'] = ta.LINEARREG_INTERCEPT(close, timeperiod=14)
    #Learn more about the Linear Regression Intercept at tadoc.org.

    #LINEARREG_SLOPE - Linear Regression Slope
    df['LINEARREG_SLOPE'] = ta.LINEARREG_SLOPE(close, timeperiod=14)
    #Learn more about the Linear Regression Slope at tadoc.org.

    #STDDEV - Standard Deviation
    df['STDDEV'] = ta.STDDEV(close, timeperiod=5, nbdev=1)
    #Learn more about the Standard Deviation at tadoc.org.

    #TSF - Time Series Forecast
    df['TSF']  = ta.TSF(close, timeperiod=14)
    #Learn more about the Time Series Forecast at tadoc.org.

    #VAR - Variance
    df['VAR'] = ta.VAR(close, timeperiod=5, nbdev=1)
    return df

def CycleIndicator(df):
    #HT_DCPERIOD - Hilbert Transform - Dominant Cycle Period
    #NOTE: The HT_DCPERIOD function has an unstable period.
    close = df['close']
    df['HT_DCPERIOD'] = ta.HT_DCPERIOD(close)
    #Learn more about the Hilbert Transform - Dominant Cycle Period at tadoc.org.

    #HT_DCPHASE - Hilbert Transform - Dominant Cycle Phase
    #NOTE: The HT_DCPHASE function has an unstable period.

    df['HT_DCPHASE'] = ta.HT_DCPHASE(close)
    #Learn more about the Hilbert Transform - Dominant Cycle Phase at tadoc.org.

    #HT_PHASOR - Hilbert Transform - Phasor Components
    #NOTE: The HT_PHASOR function has an unstable period.

    df['inphase'], df['quadrature'] = ta.HT_PHASOR(close)
    #Learn more about the Hilbert Transform - Phasor Components at tadoc.org.

    #HT_SINE - Hilbert Transform - SineWave
    #NOTE: The HT_SINE function has an unstable period.

    df['sine'], df['leadsine'] = ta.HT_SINE(close)
    #Learn more about the Hilbert Transform - SineWave at tadoc.org.

    #HT_TRENDMODE - Hilbert Transform - Trend vs Cycle Mode
    #NOTE: The HT_TRENDMODE function has an unstable period.

    df['HT_TRENDMODE'] = ta.HT_TRENDMODE(close)
    return df

def PatternRecognition(df):
    #ta.CDL2CROWS - Two Crows
    df['ta.CDL2CROWS'] =ta.CDL2CROWS(df['open'], df['high'], df['low'], df['close'])
    #ta.CDL3BLACKCROWS - Three Black Crows
    df['ta.CDL3BLACKCROWS'] = ta.CDL3BLACKCROWS(df['open'], df['high'], df['low'], df['close'])
    #ta.CDL3INSIDE - Three Inside Up/Down
    df['ta.CDL3INSIDE'] = ta.CDL3INSIDE(df['open'], df['high'], df['low'], df['close'])
    #ta.CDL3LINESTRIKE - Three-Line Strike
    df['ta.CDL3LINESTRIKE'] = ta.CDL3LINESTRIKE(df['open'], df['high'], df['low'], df['close'])
    #ta.CDL3OUTSIDE - Three Outside Up/Down
    df['ta.CDL3OUTSIDE']= ta.CDL3OUTSIDE(df['open'], df['high'], df['low'], df['close'])
    #ta.CDL3STARSINSOUTH - Three Stars In The South
    df['ta.CDL3STARSINSOUTH'] = ta.CDL3STARSINSOUTH(df['open'], df['high'], df['low'], df['close'])
    #ta.CDL3WHITESOLDIERS - Three Advancing White Soldiers
    df['ta.CDL3WHITESOLDIERS'] = ta.CDL3WHITESOLDIERS(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLABANDONEDBABY - Abandoned Baby
    df['ta.CDLABANDONEDBABY'] = ta.CDLABANDONEDBABY(df['open'], df['high'], df['low'], df['close'], penetration=0)
    #ta.CDLADVANCEBLOCK - Advance Block
    df['ta.CDLADVANCEBLOCK'] = ta.CDLADVANCEBLOCK(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLBELTHOLD - Belt-hold
    df['ta.CDLBELTHOLD'] = ta.CDLBELTHOLD(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLBREAKAWAY - Breakaway
    df['ta.CDLBREAKAWAY'] = ta.CDLBREAKAWAY(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLCLOSINGMARUBOZU - Closing Marubozu
    df['ta.CDLCLOSINGMARUBOZU'] = ta.CDLCLOSINGMARUBOZU(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLCONCEALBABYSWALL - Concealing Baby Swaldf['low']
    df['ta.CDLCONCEALBABYSWALL'] = ta.CDLCONCEALBABYSWALL(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLCOUNTERATTACK - Counterattack
    df['ta.CDLCOUNTERATTACK'] = ta.CDLCOUNTERATTACK(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLDARKCLOUDCOVER - Dark Cloud Cover
    df['ta.CDLDARKCLOUDCOVER'] = ta.CDLDARKCLOUDCOVER(df['open'], df['high'], df['low'], df['close'], penetration=0)
    #ta.CDLDOJI - Doji
    df['ta.CDLDOJI'] = ta.CDLDOJI(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLDOJISTAR - Doji Star
    df['ta.CDLDOJISTAR'] = ta.CDLDOJISTAR(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLDRAGONFLYDOJI - Dragonfly Doji
    df['ta.CDLDRAGONFLYDOJI'] = ta.CDLDRAGONFLYDOJI(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLENGULFING - Engulfing Pattern
    df['ta.CDLENGULFING'] = ta.CDLENGULFING(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLEVENINGDOJISTAR - Evening Doji Star
    df['ta.CDLEVENINGDOJISTAR'] = ta.CDLEVENINGDOJISTAR(df['open'], df['high'], df['low'], df['close'], penetration=0)
    #ta.CDLEVENINGSTAR - Evening Star
    df['ta.CDLEVENINGSTAR'] = ta.CDLEVENINGSTAR(df['open'], df['high'], df['low'], df['close'], penetration=0)
    #ta.CDLGAPSIDESIDEWHITE - Up/Down-gap side-by-side white lines
    df['ta.CDLGAPSIDESIDEWHITE'] = ta.CDLGAPSIDESIDEWHITE(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLGRAVESTONEDOJI - Gravestone Doji
    df['ta.CDLGRAVESTONEDOJI'] = ta.CDLGRAVESTONEDOJI(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLHAMMER - Hammer
    df['ta.CDLHAMMER'] = ta.CDLHAMMER(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLHANGINGMAN - Hanging Man
    df['ta.CDLHANGINGMAN'] = ta.CDLHANGINGMAN(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLHARAMI - Harami Pattern
    df['ta.CDLHARAMI'] = ta.CDLHARAMI(df['open'], df['high'], df['low'], df['close'])
    #CDLHARAMICROSS - Harami Cross Pattern
    df['CDLHARAMICROSS'] = ta.CDLHARAMICROSS(df['open'], df['high'], df['low'], df['close'])
    #CDLdf['high']WAVE - df['high']-Wave Candle
    df['CDLhighWAVE'] = ta.CDLHIGHWAVE(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLHIKKAKE - Hikkake Pattern
    df['ta.CDLHIKKAKE'] = ta.CDLHIKKAKE(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLHIKKAKEMOD - Modified Hikkake Pattern
    df['ta.CDLHIKKAKEMOD'] = ta.CDLHIKKAKEMOD(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLHOMINGPIGEON - Homing Pigeon
    df['ta.CDLHOMINGPIGEON'] = ta.CDLHOMINGPIGEON(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLIDENTICAL3CROWS - Identical Three Crows
    df['ta.CDLIDENTICAL3CROWS'] = ta.CDLIDENTICAL3CROWS(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLINNECK - In-Neck Pattern
    df['ta.CDLINNECK'] = ta.CDLINNECK(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLINVERTEDHAMMER - Inverted Hammer
    df['ta.CDLINVERTEDHAMMER'] = ta.CDLINVERTEDHAMMER(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLKICKING - Kicking
    df['ta.CDLKICKING'] = ta.CDLKICKING(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLKICKINGBYLENGTH - Kicking - bull/bear determined by the longer marubozu
    df['ta.CDLKICKINGBYLENGTH'] = ta.CDLKICKINGBYLENGTH(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLLADDERBOTTOM - Ladder Bottom
    df['ta.CDLLADDERBOTTOM'] = ta.CDLLADDERBOTTOM(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLLONGLEGGEDDOJI - Long Legged Doji
    df['ta.CDLLONGLEGGEDDOJI'] = ta.CDLLONGLEGGEDDOJI(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLLONGLINE - Long Line Candle
    df['ta.CDLLONGLINE'] = ta.CDLLONGLINE(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLMARUBOZU - Marubozu
    df['ta.CDLMARUBOZU'] = ta.CDLMARUBOZU(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLMATCHINGdf['low'] - Matching df['low']
    df['ta.CDLMATCHINGLOW'] = ta.CDLMATCHINGLOW(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLMATHOLD - Mat Hold
    df['ta.CDLMATHOLD'] = ta.CDLMATHOLD(df['open'], df['high'], df['low'], df['close'], penetration=0)
    #ta.CDLMORNINGDOJISTAR - Morning Doji Star
    df['ta.CDLMORNINGDOJISTAR'] = ta.CDLMORNINGDOJISTAR(df['open'], df['high'], df['low'], df['close'], penetration=0)
    #ta.CDLMORNINGSTAR - Morning Star
    df['ta.CDLMORNINGSTAR'] = ta.CDLMORNINGSTAR(df['open'], df['high'], df['low'], df['close'], penetration=0)
    #ta.CDLONNECK - On-Neck Pattern
    df['ta.CDLONNECK'] = ta.CDLONNECK(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLPIERCING - Piercing Pattern
    df['ta.CDLPIERCING'] = ta.CDLPIERCING(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLRICKSHAWMAN - Rickshaw Man
    df['ta.CDLRICKSHAWMAN'] = ta.CDLRICKSHAWMAN(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLRISEFALL3METHODS - Rising/Falling Three Methods
    df['ta.CDLRISEFALL3METHODS'] = ta.CDLRISEFALL3METHODS(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLSEPARATINGLINES - Separating Lines
    df['ta.CDLSEPARATINGLINES'] = ta.CDLSEPARATINGLINES(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLSHOOTINGSTAR - Shooting Star
    df['ta.CDLSHOOTINGSTAR'] = ta.CDLSHOOTINGSTAR(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLSHORTLINE - Short Line Candle
    df['ta.CDLSHORTLINE'] = ta.CDLSHORTLINE(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLSPINNINGTOP - Spinning Top
    df['ta.CDLSPINNINGTOP'] = ta.CDLSPINNINGTOP(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLSTALLEDPATTERN - Stalled Pattern
    df['ta.CDLSTALLEDPATTERN'] = ta.CDLSTALLEDPATTERN(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLSTICKSANDWICH - Stick Sandwich
    df['ta.CDLSTICKSANDWICH'] = ta.CDLSTICKSANDWICH(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLTAKURI - Takuri (Dragonfly Doji with very long df['low']er shadow)
    df['ta.CDLTAKURI'] = ta.CDLTAKURI(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLTASUKIGAP - Tasuki Gap
    df['ta.CDLTASUKIGAP'] = ta.CDLTASUKIGAP(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLTHRUSTING - Thrusting Pattern
    df['ta.CDLTHRUSTING'] = ta.CDLTHRUSTING(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLTRISTAR - Tristar Pattern
    df['ta.CDLTRISTAR'] = ta.CDLTRISTAR(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLUNIQUE3RIVER - Unique 3 River
    df['ta.CDLUNIQUE3RIVER'] = ta.CDLUNIQUE3RIVER(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLUPSIDEGAP2CROWS - Upside Gap Two Crows
    df['ta.CDLUPSIDEGAP2CROWS'] = ta.CDLUPSIDEGAP2CROWS(df['open'], df['high'], df['low'], df['close'])
    #ta.CDLXSIDEGAP3METHODS - Upside/Downside Gap Three Methods
    df['ta.CDLXSIDEGAP3METHODS'] = ta.CDLXSIDEGAP3METHODS(df['open'], df['high'], df['low'], df['close'])


    return df

def Volatility(df):
    #h=df['high'].tolist()
    #l=df['low'].tolist()
    #c=df['close'].tolist()
    #df['NATR'] = NATR(h,l,c, timeperiod=14)
    df = pd.DataFrame(data = df, dtype=np.float64)
    #print(df.head())
    #ATR - Average True Range
    #NOTE: The ATR function has an unstable period.
    high=np.array(df['high'])#.astype(int)
    low =np.array(df['low'])
    close=np.array(df['close'])
    df['ATR'] = ta.ATR(high,low,close, timeperiod=14)
    #Learn more about the Average True Range at tadoc.org.
    df['TRANGE'] = ta.TRANGE(df['high'],df['low'],df['close'])
    #df = pd.DataFrame(data = df, dtype=np.int64)
    #h=df['high'].tolist()
    #l=df['low'].tolist()
    #c=df['close'].tolist()
    df['NATR'] = ta.NATR(high,low,close, timeperiod=14)
    #Learn more about the Normalized Average True Range at tadoc.org.

    #TRANGE - True Range
    
    return df

def VolumeIndicator(df):
    #AD - Chaikin A/D Line
    df['AD'] = ta.AD(df['high'], df['low'], df['close'], df['volume'])
    #Learn more about the Chaikin A/D Line at tadoc.org.
    #df = df.dropna()  
    #ADOSC - Chaikin A/D Oscillator
    #df['ADOSC'] = ta.ADOSC(df['high'], df['low'], df['close'], df['volume'], fastperiod=3, slowperiod=10)
    #Learn more about the Chaikin A/D Oscillator at tadoc.org.

    #OBV - On Balance Volume
    #df['OBV'] = ta.OBV(df['close'], df['volume'])
    return df

def MathOperator(df):
#Math Operator Functions

    close=df['close']
    opens=df['open']
    high=df['high']
    low=df['low']
    #ADD - Vector Arithmetic Add
    df['ADD'] = ta.ADD(high, low)
    #DIV - Vector Arithmetic Div
    df['DIV'] = ta.DIV(high, low)
    #MAX - Highest value over a specified period
    df['MAX'] = ta.MAX(close, timeperiod=30)
    #MAXINDEX - Index of highest value over a specified period
    df['MAXINDEX'] = ta.MAXINDEX(close, timeperiod=30)
    #MIN - Lowest value over a specified period
    df['MIN'] = ta.MIN(close, timeperiod=30)
    #MININDEX - Index of lowest value over a specified period
    df['MININDEX'] = ta.MININDEX(close, timeperiod=30)
    #MINMAX - Lowest and highest values over a specified period
    df['min'], df['max'] = ta.MINMAX(close, timeperiod=30)
    #MINMAXINDEX - Indexes of lowest and highest values over a specified period
    df['minidx'], df['maxidx'] = ta.MINMAXINDEX(close, timeperiod=30)
    #MULT - Vector Arithmetic Mult
    df['MULT'] = ta.MULT(high, low)
    #SUB - Vector Arithmetic Substraction
    df['SUB'] = ta.SUB(high, low)
    #SUM - Summation
    df['SUM'] = ta.SUM(close, timeperiod=30)

    return df
def OverlapStudies(df):
    #Overlap Studies Functions
    print(df)
    close=df['close']
    opens=df['open']
    high=df['high']
    low=df['low']
    volume=df['volume']
    #BBANDS - Bollinger Bands
    df['upperband'], df['middleband'], df['lowerband'] = ta.BBANDS(close, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
    #Learn more about the Bollinger Bands at tadoc.org.

    #DEMA - Double Exponential Moving Average
    df['DEMA'] = ta.DEMA(close, timeperiod=30)
    #Learn more about the Double Exponential Moving Average at tadoc.org.

    #EMA - Exponential Moving Average
    #NOTE: The EMA function has an unstable period.

    df['EMA'] = ta.EMA(close, timeperiod=30)
    #Learn more about the Exponential Moving Average at tadoc.org.

    #HT_TRENDLINE - Hilbert Transform - Instantaneous Trendline
    #NOTE: The HT_TRENDLINE function has an unstable period.

    df['HT_TRENDLINE'] = ta.HT_TRENDLINE(close)
    #Learn more about the Hilbert Transform - Instantaneous Trendline at tadoc.org.

    #KAMA - Kaufman Adaptive Moving Average
    #NOTE: The KAMA function has an unstable period.

    df['KAMA'] = ta.KAMA(close, timeperiod=30)
    #Learn more about the Kaufman Adaptive Moving Average at tadoc.org.

    #MA - Moving average
    df['MA'] = ta.MA(close, timeperiod=30, matype=0)
    #MAMA - MESA Adaptive Moving Average
    #NOTE: The MAMA function has an unstable period.
    #df['mama'], df['fama'] = ta.MAMA(close, fastlimit=10, slowlimit=4)
    #Learn more about the MESA Adaptive Moving Average at tadoc.org.

    #MAVP - Moving average with variable period
    #df['MAVP'] = ta.MAVP(close, periods=8, minperiod=2, maxperiod=30, matype=0)
    #MIDPOINT - MidPoint over period
    df['MIDPOINT'] = ta.MIDPOINT(close, timeperiod=14)
    #Learn more about the MidPoint over period at tadoc.org.

    #MIDPRICE - Midpoint Price over period
    df['MIDPRICE'] = ta.MIDPRICE(high, low, timeperiod=14)
    #Learn more about the Midpoint Price over period at tadoc.org.

    #SAR - Parabolic SAR
    df['SAR'] = ta.SAR(high, low, acceleration=0, maximum=0)
    #Learn more about the Parabolic SAR at tadoc.org.

    #SAREXT - Parabolic SAR - Extended
    df['SAREXT'] = ta.SAREXT(high, low, startvalue=0, offsetonreverse=0, accelerationinitlong=0, accelerationlong=0, accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0, accelerationmaxshort=0)
    #SMA - Simple Moving Average
    df['SMA'] = ta.SMA(close, timeperiod=30)
    #Learn more about the Simple Moving Average at tadoc.org.

    #T3 - Triple Exponential Moving Average (T3)
    #NOTE: The T3 function has an unstable period.
    df['T3'] = ta.T3(close, timeperiod=5, vfactor=0)
    #Learn more about the Triple Exponential Moving Average (T3) at tadoc.org.

    #TEMA - Triple Exponential Moving Average
    df['TEMA'] = ta.TEMA(close, timeperiod=30)
    #Learn more about the Triple Exponential Moving Average at tadoc.org.

    #TRIMA - Triangular Moving Average
    df['TRIMA'] = ta.TRIMA(close, timeperiod=30)
    #Learn more about the Triangular Moving Average at tadoc.org.

    #WMA - Weighted Moving Average
    df['WMA'] = ta.WMA(close, timeperiod=30)
    #Learn more about the Weighted Moving Average at tadoc.org.

    return df 


def Momentum(df):
    close=df['close']
    opens=df['open']
    high=df['high']
    low=df['low']
    volume=df['volume']
    #Momentum Indicator Functions
    #ADX - Average Directional Movement Index
    #NOTE: The ADX function has an unstable period.

    #df['ADX'] = ADX(high, low, close, timeperiod=14)
    #Learn more about the Average Directional Movement Index at tadoc.org.

    #ADXR - Average Directional Movement Index Rating
    #NOTE: The ADXR function has an unstable period.

    df['ADXR'] = ta.ADXR(df['close'],df['high'],df['low'], timeperiod=14)
    #df['ADXR'] = ADXR(df, timeperiod=14)
    
    #Learn more about the Average Directional Movement Index Rating at tadoc.org.

    #APO - Absolute Price Oscillator
    df['APO'] = ta.APO(close, fastperiod=12, slowperiod=26, matype=0)
    #Learn more about the Absolute Price Oscillator at tadoc.org.

    #AROON - Aroon
    df['aroondown'],df['aroonup'] = ta.AROON(high, low, timeperiod=14)
    #Learn more about the Aroon at tadoc.org.

    #AROONOSC - Aroon Oscillator
    df['AROONOSC'] = ta.AROONOSC(high, low, timeperiod=14)
    #Learn more about the Aroon Oscillator at tadoc.org.

    #BOP - Balance Of Power
    df['BOP'] = ta.BOP(opens, high, low, close)
    #Learn more about the Balance Of Power at tadoc.org.

    #CCI - Commodity Channel Index
    df['CCI'] = ta.CCI(high, low, close, timeperiod=14)
    #Learn more about the Commodity Channel Index at tadoc.org.

    #CMO - Chande Momentum Oscillator
    #NOTE: The CMO function has an unstable period.

    df['CMO'] = ta.CMO(close, timeperiod=14)
    #Learn more about the Chande Momentum Oscillator at tadoc.org.

    #DX - Directional Movement Index
    #NOTE: The DX function has an unstable period.

    df['DX'] = ta.DX(high, low, close, timeperiod=14)
    #Learn more about the Directional Movement Index at tadoc.org.

    #MACD - Moving Average Convergence/Divergence
    df['macd2'], df['macdsignal2'], df['macdhist2'] = ta.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
    #Learn more about the Moving Average Convergence/Divergence at tadoc.org.

    #MACDEXT - MACD with controllable MA type
    df['macd1'],df[ 'macdsignal1'],df[ 'macdhist1'] = ta.MACDEXT(close, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0)
    #MACDFIX - Moving Average Convergence/Divergence Fix 12/26
    df['macd'], df['macdsignal'], df['macdhist'] = ta.MACDFIX(close, signalperiod=9)
    #MFI - Money Flow Index
    #NOTE: The MFI function has an unstable period.

    df['MFI'] = ta.MFI(high, low, close, volume, timeperiod=14)
    #Learn more about the Money Flow Index at tadoc.org.

    #MINUS_DI - Minus Directional Indicator
    #NOTE: The MINUS_DI function has an unstable period.

    df['MINUS_DI'] = ta.MINUS_DI(high, low, close, timeperiod=14)
    #Learn more about the Minus Directional Indicator at tadoc.org.

    #MINUS_DM - Minus Directional Movement
    #NOTE: The MINUS_DM function has an unstable period.

    df['MINUS_DM'] = ta.MINUS_DM(high, low, timeperiod=14)
    #Learn more about the Minus Directional Movement at tadoc.org.

    #MOM - Momentum
    df['MOM'] = ta.MOM(close, timeperiod=10)
    #Learn more about the Momentum at tadoc.org.

    #PLUS_DI - Plus Directional Indicator
    #NOTE: The PLUS_DI function has an unstable period.

    df['PLUS_DI'] = ta.PLUS_DI(high, low, close, timeperiod=14)
    #Learn more about the Plus Directional Indicator at tadoc.org.

    #PLUS_DM - Plus Directional Movement
    #NOTE: The PLUS_DM function has an unstable period.

    df['PLUS_DM'] = ta.PLUS_DM(high, low, timeperiod=14)
    #Learn more about the Plus Directional Movement at tadoc.org.

    #PPO - Percentage Price Oscillator
    df['PPO'] = ta.PPO(close, fastperiod=12, slowperiod=26, matype=0)
    #Learn more about the Percentage Price Oscillator at tadoc.org.

    #ROC - Rate of change : ((price/prevPrice)-1)*100
    df['ROC'] = ta.ROC(close, timeperiod=10)
    #Learn more about the Rate of change : ((price/prevPrice)-1)*100 at tadoc.org.

    #ROCP - Rate of change Percentage: (price-prevPrice)/prevPrice
    df['ROCP'] = ta.ROCP(close, timeperiod=10)
    #Learn more about the Rate of change Percentage: (price-prevPrice)/prevPrice at tadoc.org.

    #ROCR - Rate of change ratio: (price/prevPrice)
    df['ROCR'] = ta.ROCR(close, timeperiod=10)
    #Learn more about the Rate of change ratio: (price/prevPrice) at tadoc.org.

    #ROCR100 - Rate of change ratio 100 scale: (price/prevPrice)*100
    df['ROCR100'] = ta.ROCR100(close, timeperiod=10)
    #Learn more about the Rate of change ratio 100 scale: (price/prevPrice)*100 at tadoc.org.

    #RSI - Relative Strength Index
    #NOTE: The RSI function has an unstable period.

    df['RSI'] = ta.RSI(close, timeperiod=14)
    #Learn more about the Relative Strength Index at tadoc.org.

    #STOCH - Stochastic
    df['slowk'],df['slowd'] = ta.STOCH(high, low, close, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
    #Learn more about the Stochastic at tadoc.org.

    #STOCHF - Stochastic Fast
    df['shfastk'],df['shfastd'] = ta.STOCHF(high, low, close, fastk_period=5, fastd_period=3, fastd_matype=0)
    #Learn more about the Stochastic Fast at tadoc.org.

    #STOCHRSI - Stochastic Relative Strength Index
    #NOTE: The STOCHRSI function has an unstable period.

    df['fastk'],df['fastd'] = ta.STOCHRSI(close, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
    #Learn more about the Stochastic Relative Strength Index at tadoc.org.

    #TRIX - 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
    df['TRIX'] = ta.TRIX(close, timeperiod=30)
    #Learn more about the 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA at tadoc.org.

    #ULTOSC - Ultimate Oscillator
    df['ULTOSC'] = ta.ULTOSC(high, low, close, timeperiod1=7, timeperiod2=14, timeperiod3=28)
    #Learn more about the Ultimate Oscillator at tadoc.org.

    #WILLR - Williams' %R
    df['WILLR'] = ta.WILLR(high, low, close, timeperiod=14)
    return df

#df=MathTransformFunctions(df)
#print(Momentum(df))

print(StatisticFunctions(df))
print(PriceTransformFunctions(df))
print(VolumeIndicator(df))
print(MathOperator(df))
print(PatternRecognition(df))
print(CycleIndicator(df))
print(OverlapStudies(df))
print(Momentum(df))
print(MathTransformFunctions(df))


