import pandas as pd
import os

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






def load_stock_data(file_paths):
    """
    Load multiple stock CSV files and concatenate them into a single DataFrame.
    
    Parameters:
    -----------
    file_paths : list of str or dict
        List of paths to CSV files, or dict like {'AAPL': 'data/AAPL.csv', ...}
    
    Returns:
    --------
    pd.DataFrame
        Combined dataframe with 'Ticker' column, sorted by Date and Ticker
    """
    dfs = []
    
    # Handle both list of paths and dict (more flexible)
    if isinstance(file_paths, dict):
        paths_dict = file_paths
    else:
        # Assume list of paths → extract ticker from filename
        paths_dict = {}
        for path in file_paths:
            filename = os.path.basename(path)
            ticker = os.path.splitext(filename)[0]  # Removes .csv
            paths_dict[ticker] = path

    for ticker, path in paths_dict.items():
        if not os.path.exists(path):
            print(f"Warning: File not found → {path}")
            continue
            
        df = pd.read_csv(path, parse_dates=['Date'])
        
        # Basic cleaning
        df = df.sort_values('Date').reset_index(drop=True)
        df['Ticker'] = ticker
        
        # Ensure columns are in standard order
        cols_order = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Ticker']
        # In case some files have extra columns (like Adj Close), keep only main ones
        df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume'] + (['Ticker'] if 'Ticker' in df.columns else [])]
        
        dfs.append(df)
    
    if not dfs:
        raise ValueError("No data was loaded. Check your file paths.")
    
    # Concatenate all
    combined = pd.concat(dfs, ignore_index=True)
    
    # Final sort: earliest date first, then by ticker alphabetically on same date
    combined = combined.sort_values(by=['Date', 'Ticker']).reset_index(drop=True)
    
    return combined