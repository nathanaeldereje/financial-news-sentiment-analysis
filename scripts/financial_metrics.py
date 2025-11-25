"""
financial_metrics.py
====================

Clean financial metrics module using pure pandas & numpy.

Contains:
- Daily simple + log returns
- Rolling & annualized volatility
- Sharpe ratio (annualized)
- Maximum drawdown + related stats

Author: Nathanael
"""

import pandas as pd
import numpy as np


# ============================================================
# 1. RETURNS
# ============================================================

def compute_returns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute daily simple and log returns.

    Parameters
    ----------
    df : DataFrame
        Price data containing a "Close" column.

    Returns
    -------
    DataFrame
    """
    df = df.copy()
    df["return"] = df["Close"].pct_change()
    df["log_return"] = np.log(df["Close"] / df["Close"].shift(1))
    return df


# ============================================================
# 2. VOLATILITY
# ============================================================

def compute_volatility(df: pd.DataFrame, window: int = 30) -> pd.DataFrame:
    """
    Compute rolling annualized volatility based on log returns.

    Annualized Vol = rolling_std * sqrt(252)
    """
    df = df.copy()
    df[f"vol_{window}"] = df["log_return"].rolling(window).std() * np.sqrt(252)
    return df


# ============================================================
# 3. SHARPE RATIO
# ============================================================

def compute_sharpe(df: pd.DataFrame, risk_free_rate: float = 0.03) -> float:
    """
    Compute annualized Sharpe Ratio.

    Uses log returns (more stable mathematically).
    """
    df = df.dropna(subset=["log_return"])

    mean_ann = df["log_return"].mean() * 252
    vol_ann = df["log_return"].std() * np.sqrt(252)

    if vol_ann == 0:
        return 0.0

    return (mean_ann - risk_free_rate) / vol_ann


# ============================================================
# 4. MAX DRAWDOWN
# ============================================================

def compute_drawdown(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute cumulative return, running max, and drawdown series.

    Drawdown = (CumReturn / RollingMax) - 1
    """
    df = df.copy()
    df["cum_return"] = (1 + df["return"]).cumprod()
    df["running_max"] = df["cum_return"].cummax()
    df["drawdown"] = df["cum_return"] / df["running_max"] - 1
    return df
