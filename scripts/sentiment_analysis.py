from textblob import TextBlob
import pandas as pd
from typing import Callable

def get_sentiment(text: str) -> float:
    """
    Compute sentiment polarity of a text using TextBlob.

    Args:
        text (str): Input headline or text

    Returns:
        float: Sentiment score between -1.0 (negative) and +1.0 (positive)
               Returns 0.0 for invalid/empty input
    """
    if not isinstance(text, str) or text.strip() == "":
        return 0.0
    return TextBlob(text).sentiment.polarity


def add_sentiment_scores(df: pd.DataFrame, text_column: str = "headline") -> pd.DataFrame:
    """
    Apply sentiment analysis to a text column in the DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame containing text
        text_column (str): Name of column containing text (default: 'headline')

    Returns:
        pd.DataFrame: Original DataFrame with new 'sentiment_score' column
    """
    df = df.copy()
    df["sentiment_score"] = df[text_column].apply(get_sentiment)
    return df


def aggregate_daily_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate sentiment scores by date and stock (mean per day).

    Args:
        df (pd.DataFrame): DataFrame with 'Date', 'stock', and 'sentiment_score'

    Returns:
        pd.DataFrame: Daily average sentiment per stock
    """
    daily = (
        df.groupby(["Date", "stock"], as_index=False)["sentiment_score"]
          .mean()
          .rename(columns={"sentiment_score": "avg_sentiment"})
    )
    return daily