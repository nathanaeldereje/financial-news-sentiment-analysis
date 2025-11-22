import pandas as pd

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