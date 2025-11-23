"""
technical_indicators.py

Calculate common technical indicators using pandas-ta (pure Python, no compilation needed).
Fully compatible with pandas MultiIndex/groupby and works in any environment.
"""

from __future__ import annotations
import pandas as pd
import pandas_ta as ta  # type: ignore


def add_ta_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add popular technical indicators to stock price data.

    Parameters
    ----------
    df : pd.DataFrame
        Must contain columns: ['Open', 'High', 'Low', 'Close', 'Volume']
        Optional: 'Ticker' column for multi-ticker support

    Returns
    -------
    pd.DataFrame
        Original dataframe with new indicator columns:
            SMA_20, SMA_50, EMA_20, RSI_14, MACD_12_26_9, MACD_signal_12_26_9, MACD_hist_12_26_9
    """
    df = df.copy()

    # Ensure proper column names and sorting
    required_cols = ["Open", "High", "Low", "Close", "Volume"]
    if not all(col in df.columns for col in required_cols):
        raise ValueError(f"DataFrame must contain columns: {required_cols}")

    # If multi-ticker data, apply indicators per ticker
    if "Ticker" in df.columns:
        df = df.sort_values(["Ticker", "Date"])

        # Simple Moving Averages
        df["SMA_20"] = df.groupby("Ticker")["Close"].transform(
            lambda x: ta.sma(x, length=20)
        )
        df["SMA_50"] = df.groupby("Ticker")["Close"].transform(
            lambda x: ta.sma(x, length=50)
        )

        # Exponential Moving Average
        df["EMA_20"] = df.groupby("Ticker")["Close"].transform(
            lambda x: ta.ema(x, length=20)
        )

        # RSI
        df["RSI_14"] = df.groupby("Ticker")["Close"].transform(
            lambda x: ta.rsi(x, length=14)
        )

        # MACD (returns a DataFrame with macd, histogram, signal)
        macd = df.groupby("Ticker", group_keys=False)["Close"].apply(
            lambda x: ta.macd(x, fast=12, slow=26, signal=9)
        )

        # Rename columns to match old naming convention
        macd.columns = ["MACD_12_26_9", "MACD_hist_12_26_9", "MACD_signal_12_26_9"]
        df = pd.concat([df.reset_index(drop=True), macd.reset_index(drop=True)], axis=1)

    else:
        # Single ticker case
        df["SMA_20"] = ta.sma(df["Close"], length=20)
        df["SMA_50"] = ta.sma(df["Close"], length=50)
        df["EMA_20"] = ta.ema(df["Close"], length=20)
        df["RSI_14"] = ta.rsi(df["Close"], length=14)

        macd = ta.macd(df["Close"], fast=12, slow=26, signal=9)
        macd.columns = ["MACD_12_26_9", "MACD_hist_12_26_9", "MACD_signal_12_26_9"]
        df = pd.concat([df, macd], axis=1)

    return df