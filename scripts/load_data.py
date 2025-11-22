import pandas as pd

def load_and_preprocess_data(path="../data/raw_analyst_ratings.csv") -> pd.DataFrame:
    """
    Load the raw Benzinga analyst ratings dataset and perform initial preprocessing.
    
    Parameters
    ----------
    path : str, default "../data/raw_analyst_ratings.csv"
        Path to the CSV file.
    
    Returns
    -------
    pd.DataFrame
        Cleaned dataframe with additional features:
        - headline_length
        - year, weekday, hour
        - normalized UTC date (naive timestamp)
    """
    df = pd.read_csv(path, parse_dates=["date"], index_col=0)
    
    # Handle timezone-aware timestamps properly
    df['date'] = pd.to_datetime(df['date'],format='mixed', utc=True)
    df['date'] = df['date'].dt.tz_convert('UTC').dt.tz_localize(None)
    
    # Feature engineering
    df['headline_length'] = df['headline'].astype(str).apply(len)
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['weekday'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['date_only'] = df['date'].dt.date
    
    return df