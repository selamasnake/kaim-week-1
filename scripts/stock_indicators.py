import  utils as util
import talib
import pynance as data

class IndicatorCalculator:
    """
    Class for calculating technical indicators stock price data.
    """

    def calculate_technical_indicators(data):
        """
        Calculate common technical indicators using TA-Lib.

        Indicators:
        - SMA (Simple Moving Average)
        - EMA (Exponential Moving Average)
        - RSI (Relative Strength Index)
        - MACD (Moving Average Convergence Divergence)

        """
        ##Simple Moving Average
        data['SMA_20'] = talib.SMA(data['Close'], timeperiod=20)
        data['SMA_50'] = talib.SMA(data['Close'], timeperiod=50)

        ##Exponential Moving Average
        data['EMA_20'] = talib.SMA(data['Close'], timeperiod=20)
        data['EMA_50'] = talib.SMA(data['Close'], timeperiod=50)

        ##Relative Strength Index
        data['RSI_14'] = talib.RSI(data['Close'], timeperiod=14)

        ##MACD (Moving Average Convergence Divergence)
        macd, macdsignal, macd_hist = talib.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)

        # Add the MACD and Signal line to your DataFrame
        data['MACD'] = macd
        data['MACDSignal'] = macdsignal
        data["MACD_hist"] = macd_hist

        return data


