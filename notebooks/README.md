# Notebooks

This folder contains Jupyter notebooks for exploratory analysis and reporting.

## Current Notebooks

### 01_eda.ipynb ★ (Task 1 – Main Deliverable)
- High-level, clean, presentation-ready notebook
- Uses modular functions from `../scripts/`
- Contains all required EDA with visualizations and conclusions
- Designed to be shared with stakeholders or evaluators

### 02_quant_analysis.ipynb ★ (Task 2 – In Progress)
- Quantitative stock analysis using TA-Lib and PyNance
- Currently at **Technical Indicators phase** (SMA, EMA, RSI, MACD)
- Uses modular function `add_ta_indicators` from `../scripts/technical_indicators.py`
- Will later include visualizations and financial metrics

### Future Notebooks (Planned)
- 03_sentiment_analysis.ipynb – Sentiment analysis of financial news headlines
- 04_predictive_modeling.ipynb – Predictive models for stock or sentiment forecasting

## How to Run
1. Install requirements: `pip install -r requirements.txt`
2. Launch Jupyter: `jupyter notebook` or `jupyter lab`
3. Open the desired notebook (e.g., `01_eda.ipynb` or `02_quant_analysis.ipynb`)
