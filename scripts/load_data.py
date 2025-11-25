import pandas as pd
from typing import Tuple


def load_data(path) -> pd.DataFrame:
    """
    Load the raw Benzinga analyst ratings dataset.
    
    Parameters
    ----------
    path : str, 
        Path to the CSV file.
    
    Returns
    -------
    pd.DataFrame
        - normalized UTC date (naive timestamp)
    """
    df = pd.read_csv(path, parse_dates=["date"], index_col=0)
    # Handle timezone-aware timestamps properly
    df['date'] = pd.to_datetime(df['date'],format='mixed', utc=True)
    df['date'] = df['date'].dt.tz_convert('UTC').dt.tz_localize(None)
    return df

def preprocess_data(df):
    """
    perform initial preprocessing. 
    Parameters
    ----------
    pd.DataFrame
    
    Returns
    -------
    pd.DataFrame
        Cleaned dataframe with additional features:
        - headline_length
        - year, weekday, hour
    """
    # Feature engineering
    df['headline_length'] = df['headline'].astype(str).apply(len)
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['weekday'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['date_only'] = df['date'].dt.date
    return df



def load_and_prepare_full_stocks(path: str) -> pd.DataFrame:
    """
    Load stock price data and compute daily returns.

    Args:
        path (str): Path to the processed stocks CSV file.

    Returns:
        pd.DataFrame: DataFrame with columns ['Date', 'Ticker', 'Close', 'Daily_Return']
                      sorted by Ticker and Date, with NaN returns removed.
    
    Note:
        Daily return = (Close_t / Close_{t-1}) - 1
        First row per ticker is dropped due to NaN return.
    """
    df = pd.read_csv(path, parse_dates=["Date"])
    
    # Keep only relevant columns and ensure correct order
    df = df[["Date", "Ticker", "Close"]].copy()
    df = df.sort_values(['Ticker', 'Date']).reset_index(drop=True)
    
    # Calculate percentage change in closing price
    df['Daily_Return'] = df.groupby('Ticker')['Close'].pct_change()
    
    # Remove rows where return cannot be computed (first day of each stock)
    df.dropna(subset=['Daily_Return'], inplace=True)
    
    return df




def load_and_prepare_news(path: str) -> pd.DataFrame:
    """
    Load cleaned analyst ratings/news data.

    Args:
        path (str): Path to the cleaned news CSV file.

    Returns:
        pd.DataFrame: DataFrame with columns ['Date', 'headline', 'stock']
                      Date column properly parsed and renamed.
    """
    df = pd.read_csv(path, parse_dates=["date"], index_col=0)
    df.rename(columns={"date": "Date"}, inplace=True)
    
    # Select only needed columns
    df = df[["Date", "headline", "stock"]].copy()
    
    return df





def align_news_with_stocks(news: pd.DataFrame, stocks: pd.DataFrame) -> pd.DataFrame:
    """
    Filter news to only include entries on trading days and for valid tickers.

    Args:
        news (pd.DataFrame): Raw news DataFrame with 'Date' and 'stock'
        stocks (pd.DataFrame): Prepared stocks DataFrame with 'Date' and 'Ticker'

    Returns:
        pd.DataFrame: Filtered news DataFrame matching stock data availability
    """
    trading_days = stocks["Date"].unique()
    valid_tickers = stocks["Ticker"].unique()
    
    aligned_news = news[
        news["Date"].isin(trading_days) &
        news["stock"].isin(valid_tickers)
    ].copy()
    
    print(f"Aligned news: {len(aligned_news):,} rows (from {len(news):,})")
    return aligned_news