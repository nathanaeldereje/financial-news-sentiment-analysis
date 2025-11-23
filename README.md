# Financial News Sentiment Analysis – Task 1 & Task 2 Progress

**Goal**: Analyze financial news headlines (~1.4M records in `FNSPID/raw_analyst_ratings.csv`) and perform quantitative stock analysis using Python, TA-Lib, and PyNance.  

---

## Current Status

**Task 1 – EDA & Repository Setup** ✓ Completed  
- Branch: `task-1`  
- Main notebook: `notebooks/01_eda.ipynb`  

**Task 2 – Quantitative Analysis (Ongoing)**  
- Branch: `task-2`  
- Main notebook: `notebooks/02_quant_analysis.ipynb`  
- Current phase: **Technical Indicators with TA-Lib** (SMA, EMA, RSI, MACD)  
- Modular function `add_ta_indicators` moved to `scripts/technical_indicators.py`  

---

## Quick Start (One-command setup)

```bash
git clone https://github.com/yourusername/financial-news-sentiment-analysis.git
cd financial-news-sentiment-analysis
pip install -r requirements.txt
jupyter lab notebooks/01_eda.ipynb




Project Structure
├── data/
│   ├── raw/raw_analyst_ratings.csv
│   └── processed/raw_analyst_ratings_clean.csv
├── notebooks/
│   ├── 01_eda.ipynb          ← Task 1 deliverable (EDA)
│   └── 02_quant_analysis.ipynb ← Task 2 (Quant Analysis, in progress)
├── scripts/                  
│   ├── load_data.py
│   ├── technical_indicators.py ← TA-Lib indicators (SMA, EMA, RSI, MACD)
│   ├── publisher_analysis.py
│   ├── text_analysis.py
│   └── __init__.py
├── tests/                    
├── requirements.txt
├── .gitignore
└── README.md                 


Scripts Usage Example
from scripts.load_data import load_data, preprocess_data
from scripts.technical_indicators import add_ta_indicators
from scripts.publisher_analysis import publisher_analysis
from scripts.text_analysis import run_topic_modeling, extract_keywords

# Task 1
df = load_data("../data/raw/raw_analyst_ratings.csv")
df = preprocess_data(df)
publisher_analysis(df)
keywords = extract_keywords(df, top_n=30)
run_topic_modeling(df, n_topics=20)

# Task 2 (partial)
stocks_ta = add_ta_indicators(stocks)

Key Findings (Task 1 Summary)
- Average headline length: 73 characters (σ = 40.7)
- Top publisher: Paul Quintaro (228k articles), followed by Lisa Levin
- Massive spike on 2020-03-12 → 2,739 articles (Black Thursday – worst single-day drop since 1987)
- Peak publishing hour: 00:00 UTC (scheduled Benzinga automated posts)
- 20 dominant topics discovered via NMF (52-week highs/lows, earnings, upgrades/downgrades, pre-market movers, etc.)
