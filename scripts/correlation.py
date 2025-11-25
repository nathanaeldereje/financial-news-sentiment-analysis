import pandas as pd
from typing import Dict

def merge_sentiment_and_returns(
    sentiment_df: pd.DataFrame,
    stocks_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Inner join daily sentiment with stock returns on Date and Ticker/stock.

    Args:
        sentiment_df (pd.DataFrame): Daily aggregated sentiment
        stocks_df (pd.DataFrame): Stock data with Daily_Return

    Returns:
        pd.DataFrame: Merged dataset ready for correlation analysis
    """
    merged = pd.merge(
        sentiment_df,
        stocks_df[['Date', 'Ticker', 'Daily_Return']],
        left_on=['Date', 'stock'],
        right_on=['Date', 'Ticker'],
        how='inner'
    )
    merged.drop(columns=['Ticker'], inplace=True)
    merged.dropna(subset=['Daily_Return'], inplace=True)
    
    print(f"Merged dataset: {len(merged):,} matched day-stock pairs")
    return merged


def compute_correlations(merged: pd.DataFrame) -> Dict[str, float]:
    """
    Compute same-day and next-day correlations between sentiment and returns.

    Args:
        merged (pd.DataFrame): Merged sentiment + returns DataFrame

    Returns:
        dict: Pearson, Spearman, and next-day Pearson correlations
    """
    pearson = merged[['avg_sentiment', 'Daily_Return']].corr().iloc[0, 1]
    spearman = merged[['avg_sentiment', 'Daily_Return']].corr(method='spearman').iloc[0, 1]
    
    # Next-day return (does today's news predict tomorrow's move?)
    merged['Daily_Return_next'] = merged.groupby('stock')['Daily_Return'].shift(-1)
    lagged = merged[['avg_sentiment', 'Daily_Return_next']].corr().iloc[0, 1]
    
    return {
        "pearson_same_day": round(pearson, 4),
        "spearman_same_day": round(spearman, 4),
        "pearson_next_day": round(lagged, 4) if not pd.isna(lagged) else None
    }