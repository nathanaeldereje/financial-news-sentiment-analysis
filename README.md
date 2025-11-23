# Financial News Sentiment Analysis – Task 1: EDA & Repository Setup

**Goal**: Perform comprehensive Exploratory Data Analysis on ~1.4M financial news headlines (FNSPID/raw_analyst_ratings.csv) and set up a clean, professional Python project structure with Git best practices.

**Current Status**: Task 1 Completed ✓  
Branch: `task-1` | Main EDA notebook: `notebooks/01_eda.ipynb`

## Quick Start (One-command setup)

    ```bash
    git clone https://github.com/yourusername/financial-news-sentiment-analysis.git
    cd financial-news-sentiment-analysis
    pip install -r requirements.txt
    jupyter lab notebooks/01_eda.ipynb

    ├── data/
    │   ├── raw/raw_analyst_ratings.csv
    │   └── processed/raw_analyst_ratings_clean.csv
    ├── notebooks/
    │   └── 01_eda.ipynb          ← Main deliverable (clean, presentation-ready)
    ├── scripts/                  ← Reusable modular functions
    │   ├── load_data.py
    │   ├── publisher_analysis.py
    │   ├── text_analysis.py
    │   └── __init__.py
    ├── tests/                    ← Unit tests (will grow in later tasks)
    ├── requirements.txt
    ├── .gitignore
    └── README.md                 ← you are here


## Scripts Usage Example
    from scripts.load_data import load_data, preprocess_data
    from scripts.publisher_analysis import publisher_analysis
    from scripts.text_analysis import run_topic_modeling, extract_keywords

    df = load_data("../data/raw/raw_analyst_ratings.csv")
    df = preprocess_data(df)
    publisher_analysis(df)
    keywords = extract_keywords(df, top_n=30)
    run_topic_modeling(df, n_topics=20)

Key Findings (Summary of EDA)

    Average headline length: 73 characters (σ = 40.7)
    Top publisher: Paul Quintaro (228k articles), followed by Lisa Levin
    Massive spike on 2020-03-12 → 2,739 articles (Black Thursday – worst single-day drop since 1987)
    Peak publishing hour: 00:00 UTC (scheduled Benzinga automated posts)
    20 dominant topics discovered via NMF (52-week highs/lows, earnings, upgrades/downgrades, pre-market movers, etc.)

Full analysis + visualizations in notebooks/01_eda.ipy