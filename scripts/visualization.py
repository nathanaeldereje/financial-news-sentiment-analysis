import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_sentiment_vs_return(merged: pd.DataFrame) -> None:
    """Scatter plot with regression line showing relationship between sentiment and return."""
    plt.figure(figsize=(10, 6))
    sns.regplot(
        x='avg_sentiment', y='Daily_Return',
        data=merged, scatter_kws={'alpha': 0.4}, line_kws={'color': 'red'}
    )
    plt.title("Daily Stock Return vs Average News Sentiment", fontsize=14, pad=15)
    plt.xlabel("Average Daily Sentiment Score (TextBlob)")
    plt.ylabel("Daily Return")
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
    plt.grid(True, alpha=0.3)
    plt.show()


def plot_sentiment_distribution(merged: pd.DataFrame) -> None:
    """Distribution of average daily sentiment scores."""
    plt.figure(figsize=(10, 5))
    sns.histplot(merged['avg_sentiment'], bins=50, kde=True, color="steelblue", alpha=0.7)
    plt.title("Distribution of Average Daily Sentiment Scores", fontsize=14, pad=15)
    plt.xlabel("Sentiment Score")
    plt.ylabel("Frequency")
    plt.axvline(merged['avg_sentiment'].mean(), color='red', linestyle='--', 
                label=f"Mean: {merged['avg_sentiment'].mean():.3f}")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()