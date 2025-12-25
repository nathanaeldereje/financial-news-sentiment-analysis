# Financial News Sentiment Analysis for Stock Price Prediction

**Project Goal**  
Analyze the impact of financial news sentiment on stock price movements using the FNSPID dataset (~1.4M Benzinga headlines, 2011–2020) integrated with daily OHLCV data for **AAPL**, **GOOG**, **META**, **MSFT**, and **NVDA**. The project builds a reproducible Python pipeline covering Exploratory Data Analysis (EDA), technical indicators, sentiment scoring, and correlation analysis to inform predictive strategies for Nova Financial Solutions.

**Status**: All Week 1 Tasks Completed ✓  
**Branches**: `task-1` (EDA), `task-2` (Technical Analysis), `task-3` (Sentiment & Correlation) → Merged to `main` via PRs  

**Main Notebooks**  
- `notebooks/01_eda.ipynb` – Task 1  
- `notebooks/02_technical_analysis.ipynb` – Task 2  
- `notebooks/03_sentiment_correlation.ipynb` – Task 3  

## Quick Start

```bash
git clone https://github.com/yourusername/financial-news-sentiment-analysis.git
cd financial-news-sentiment-analysis
pip install -r requirements.txt
jupyter lab  # Open the notebooks
```
## Project Structure
```text
├── data/
│   ├── raw/
│   │   └── raw_analyst_ratings.csv                  # Original news dataset
│   └── processed/
│       ├── raw_analyst_ratings_clean.csv            # Cleaned news data
│       ├── stocks_full.csv                           # Enriched stock data with indicators
│       └── news_stock_merged.csv                     # Aligned news + stock returns
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_technical_analysis.ipynb
│   └── 03_sentiment_correlation.ipynb
├── scripts/                                         # Modular, reusable functions
│   ├── load_data.py
│   ├── publisher_analysis.py
│   ├── text_analysis.py
│   ├── technical_indicators.py
│   ├── sentiment_analysis.py
│   └── alignment.py
├── tests/                                           # Unit tests
├── .github/workflows/                               # GitHub Actions CI/CD
├── requirements.txt
├── .gitignore
└── README.md                                        # You are here
```
# Quantitative Stock Analysis & Sentiment Correlation Report

## Key Findings Summary

### Task 1: Exploratory Data Analysis
* **Dataset:** 1,407,328 headlines after cleaning.
* **Headline Characteristics:** Mean length of 73 characters (median 64, highly right-skewed).
* **Temporal Patterns:**
    * Steady growth in news volume 2011–2019, massive surge early 2020 (COVID-19).
    * **Highest single-day volume:** March 12, 2020 ("Black Thursday") – 2,739 articles.
    * **Peak publishing hour:** 00:00 UTC (likely automated/scheduled posts).
    * Very low volume on weekends.
* **Publisher Concentration:** Top 5 publishers (Paul Quintaro, Lisa Levin, Benzinga Newsdesk, etc.) account for >60% of articles.
* **Topic Modeling (NMF, 20 topics):**
    * Headlines follow highly templated patterns.
    * **Dominant themes:** 52-week highs/lows, analyst upgrades/downgrades, earnings vs. estimates, premarket movers, price-target changes.

---

### Task 2: Technical Indicators & Quantitative Analysis
* **Stocks Analyzed:** AAPL, GOOG, META (from 2012), MSFT, NVDA (daily OHLCV 2009–2023).
* **Indicators Implemented (via TA-Lib):**
    * **Moving Averages:** 20/50-day SMA, 20-day EMA.
    * **Momentum:** RSI (14-day).
    * **Trend:** MACD (12,26,9).
* **Risk Metrics:**
    * 30-day rolling volatility.
    * Cumulative returns & drawdowns.
    * **Sharpe Ratios (rf=0):** AAPL highest at **0.89**; others lower due to early volatility.
* **Visualizations:** Publication-ready charts generated for each ticker (price + overlays, RSI, MACD, volatility, drawdowns).



---

### Task 3: Sentiment Analysis & Correlation with Returns
* **Alignment:** Filtered to ticker-specific headlines (4,624 rows) $\rightarrow$ 1,527 matched trading days with both news and price data.
* **Sentiment Scoring:** TextBlob polarity ($-1$ to $+1$), aggregated as daily mean per ticker.
* **Correlation Results:**
    | Metric | Pearson Correlation | Spearman Correlation |
    | :--- | :--- | :--- |
    | **Same-day Sentiment $\rightarrow$ Return** | +0.0992 | +0.1266 |
    | **Next-day Sentiment $\rightarrow$ Return** | -0.0167 | N/A |

* **Insight:** News sentiment acts as a **contemporaneous signal** rather than a leading indicator in this dataset.

---

## Overall Insights & Recommendations

* **News volume** is a strong proxy for market stress (e.g., extreme spikes during March 2020 crash).
* **Benzinga headlines** are highly formulaic $\rightarrow$ excellent for structured topic extraction.
* **Sentiment** shows weak but positive same-day correlation with returns, offering potential tactical edge on high-volume news days.

### Recommendation for Nova Financial Solutions
> **Use aggregated daily sentiment as a same-day sentiment overlay for risk management or intraday tactical positioning.** Avoid relying on it for next-day directional predictions.

---

## Future Improvements
* Adopt domain-specific NLP models (e.g., **FinBERT**).
* Incorporate intraday price data and multi-source news.
* Build sequence models (**LSTM/Transformer**) and rigorous backtesting framework.

*All code is modular, tested, and reproducible. CI/CD via GitHub Actions ensures pipeline stability.*orrelation Results:**
    * **Same-Day Sentiment → Return:** Pearson **+0.0992**, Spearman **+0.1266**. This indicates a modest, positive contemporaneous relationship.
    * **Next-Day Sentiment → Return:** Pearson **-0.0167**. This is essentially zero, indicating no predictive power.


Challenge completed – Nov 25 2025 Built by Nathanael Dereje
