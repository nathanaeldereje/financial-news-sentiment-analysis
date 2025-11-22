import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def extract_article_type(url: str) -> str:
    """Extract semantic article type from Benzinga URL path."""
    if not isinstance(url, str):
        return "unknown"
    try:
        path = url.split('benzinga.com/')[-1].split('/')[0]
        if path.startswith('news'): return "General News"
        elif path in ['analyst-ratings', 'trading-ideas']: return "Analyst Ratings"
        elif 'movers' in path: return "Movers"
        elif 'earnings' in path: return "Earnings"
        elif 'options' in path: return "Options"
        elif path in ['general-market', 'stock-market-updates']: return "Market Summary"
        else: return "Other"
    except:
        return "Other"

def publisher_analysis(df: pd.DataFrame):
    """
    Perform complete publisher analysis including:
    - Top publishers by volume
    - Article type extraction from URL
    - Heatmap showing content specialization
    
    Parameters
    ----------
    df : pd.DataFrame
        Must contain 'publisher' and 'url' columns
    """
    df['article_type'] = df['url'].apply(extract_article_type)
    
    print("Top 15 Publishers:")
    print(df['publisher'].value_counts().head(15))
    
    top10 = df['publisher'].value_counts().head(10).index
    cross = pd.crosstab(df['publisher'], df['article_type'])
    cross_pct = cross.div(cross.sum(1), axis=0) * 100
    cross_pct = cross_pct.loc[top10]

    plt.figure(figsize=(12, 8))
    sns.heatmap(cross_pct.T, annot=True, fmt='.1f', cmap='YlGnBu')
    plt.title('Article Type Distribution by Top 10 Publishers (%)')
    plt.ylabel('Article Type')
    plt.xlabel('Publisher')
    plt.tight_layout()
    plt.show()