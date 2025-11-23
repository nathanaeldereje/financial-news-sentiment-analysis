# Scripts Module
This folder contains reusable, modular Python scripts for the entire project.

## Files

- `__init__.py`  
  Makes `scripts` a proper Python package so you can do `from scripts.load_data import ...`

- `load_data.py`  
  Loads and performs initial preprocessing on `raw_analyst_ratings.csv`  
  Returns a cleaned DataFrame with essential features (date normalized, headline_length, year, weekday, hour, etc.)

- `utils.py`  
  Helper functions, primarily `clean_text()` used for NLP preprocessing.

- `publisher_analysis.py`  
  - Extracts article type from Benzinga URLs  
  - Performs detailed publisher vs article-type analysis  
  - Generates the key insight heatmap

- `text_analysis.py`  
  Runs full text preprocessing + NMF topic modeling on headlines.

- `descriptive_stats.py` *(optional future)*  
- `time_analysis.py` *(optional future)*

## Usage Example (in notebooks)
```python
from scripts.load_data import load_and_preprocess_data
from scripts.publisher_analysis import publisher_analysis
from scripts.text_analysis import run_topic_modeling

df = load_and_preprocess_data()
publisher_analysis(df)
run_topic_modeling(df, n_topics=20)