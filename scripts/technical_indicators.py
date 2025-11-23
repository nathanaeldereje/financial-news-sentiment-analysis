"""
technical_indicators.py

Module to calculate common technical indicators for stock data using TA-Lib.
"""

import pandas as pd
import talib

def add_ta_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add technical indicators (SMA, EMA, RSI, MACD) to a multi-ticker stock DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        Stock data containing columns: ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Ticker']

    Returns
    -------
    pd.DataFrame
        DataFrame with added columns:
        ['SMA_20', 'SMA_50', 'EMA_20', 'RSI_14', 'MACD', 'MACD_signal', 'MACD_hist']
    """

    # Make a copy to avoid changing the original DataFrame
    df = df.copy()

    # ------------------------------
    # Moving Averages
    # ------------------------------
    df["SMA_20"] = df.groupby("Ticker")["Close"].transform(lambda x: talib.SMA(x, timeperiod=20))
    df["SMA_50"] = df.groupby("Ticker")["Close"].transform(lambda x: talib.SMA(x, timeperiod=50))
    df["EMA_20"] = df.groupby("Ticker")["Close"].transform(lambda x: talib.EMA(x, timeperiod=20))

    # ------------------------------
    # Relative Strength Index
    # ------------------------------
    df["RSI_14"] = df.groupby("Ticker")["Close"].transform(lambda x: talib.RSI(x, timeperiod=14))

    # ------------------------------
    # MACD (Momentum Indicator)
    # ------------------------------
    def macd_group(x):
        macd, signal, hist = talib.MACD(x, fastperiod=12, slowperiod=26, signalperiod=9)
        return pd.DataFrame({"MACD": macd, "MACD_signal": signal, "MACD_hist": hist})

    macd_df = df.groupby("Ticker")["Close"].apply(macd_group)
    macd_df.index = macd_df.index.droplevel(0)  # flatten MultiIndex
    df = pd.concat([df, macd_df], axis=1)

    return df
