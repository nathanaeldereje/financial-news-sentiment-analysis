# Scripts Module

This folder contains reusable, modular Python scripts for the entire project.

## Current Files

- `__init__.py`  
  Makes `scripts` a proper Python package so you can do `from scripts.load_data import ...`

- `load_data.py`  
  - Loads and preprocesses `raw_analyst_ratings.csv`  
  Returns a cleaned DataFrame with essential features (date normalized, headline_length, year, weekday, hour, etc.)
  - load_stock_data like `AAPL.csv`  
  Load multiple stock CSV files and concatenate them into a single DataFrame then returns it.


- `technical_indicators.py` ★ (Task 2 – In Progress)  
  Contains `add_ta_indicators(df)`  
  Adds TA-Lib technical indicators per ticker: SMA, EMA, RSI, MACD

- `utils.py`  
  Helper functions, primarily `clean_text()` used for NLP preprocessing

- `publisher_analysis.py`  
  - Extracts article type from Benzinga URLs  
  - Performs detailed publisher vs article-type analysis  
  - Generates the key insight heatmap

- `text_analysis.py`  
  Runs full text preprocessing + NMF topic modeling on headlines

- `descriptive_stats.py` *(optional future)*  
- `time_analysis.py` *(optional future)*

## Usage Example (in notebooks)
```python
from scripts.load_data import load_data, preprocess_data
from scripts.technical_indicators import add_ta_indicators
from scripts.publisher_analysis import publisher_analysis
from scripts.text_analysis import run_topic_modeling

# Task 1
df = load_data("../data/raw/raw_analyst_ratings.csv")
df = preprocess_data(df)
publisher_analysis(df)
run_topic_modeling(df, n_topics=20)

# Task 2 (partial)
stocks_ta = add_ta_indicators(stocks)
