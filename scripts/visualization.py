"""
visualization.py

Modular plotting functions for stock prices and technical indicators.
Author: Nathanael
"""

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


sns.set_style("whitegrid")


def plot_price_and_sma(df, ticker: str):
    """
    Plot closing price with SMA_20 and SMA_50 for a ticker.
    """
    df_t = df[df['Ticker'] == ticker].dropna(subset=['SMA_20', 'SMA_50'])
    plt.figure(figsize=(14,6))
    plt.plot(df_t['Date'], df_t['Close'], label='Close', color='blue')
    plt.plot(df_t['Date'], df_t['SMA_20'], label='SMA 20', color='orange')
    plt.plot(df_t['Date'], df_t['SMA_50'], label='SMA 50', color='green')
    plt.title(f"{ticker} Price vs SMA")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()


def plot_rsi(df, ticker: str):
    """
    Plot RSI_14 with overbought/oversold lines.
    """
    df_t = df[df['Ticker'] == ticker].dropna(subset=['RSI_14'])
    plt.figure(figsize=(14,4))
    plt.plot(df_t['Date'], df_t['RSI_14'], label='RSI 14', color='purple')
    plt.axhline(70, color='red', linestyle='--', label='Overbought')
    plt.axhline(30, color='green', linestyle='--', label='Oversold')
    plt.title(f"{ticker} RSI")
    plt.xlabel("Date")
    plt.ylabel("RSI")
    plt.legend()
    plt.show()


def plot_macd(df, ticker: str):
    """
    Plot MACD line, signal line, and histogram.
    """
    df_t = df[df['Ticker'] == ticker].dropna(subset=['MACD_12_26_9'])
    plt.figure(figsize=(14,5))
    plt.bar(df_t['Date'], df_t['MACD_hist_12_26_9'], 
            label='Histogram', 
            width=5,   # widen bars
            alpha=0.6,
            color='green')   # transparency helps visibility
    plt.plot(df_t['Date'], df_t['MACD_12_26_9'], label='MACD', color='blue')
    plt.plot(df_t['Date'], df_t['MACD_signal_12_26_9'], label='Signal', color='red')


    plt.title(f"{ticker} MACD")
    plt.xlabel("Date")
    plt.legend()
    plt.show()


def plot_volatility(df, ticker: str):
    """
    Plot rolling volatility.
    """
    df_t = df[df['Ticker'] == ticker].dropna(subset=['vol_30'])
    plt.figure(figsize=(14,4))
    plt.plot(df_t['Date'], df_t['vol_30'], label='30-day Volatility', color='brown')
    plt.title(f"{ticker} Rolling Volatility")
    plt.xlabel("Date")
    plt.ylabel("Volatility")
    plt.legend()
    plt.show()


def plot_drawdown(df, ticker: str):
    """
    Plot drawdown series.
    """
    df_t = df[df['Ticker'] == ticker].dropna(subset=['drawdown'])
    plt.figure(figsize=(14,4))
    plt.plot(df_t['Date'], df_t['drawdown'], label='Drawdown', color='red')
    plt.title(f"{ticker} Drawdown")
    plt.xlabel("Date")
    plt.ylabel("Drawdown")
    plt.legend()
    plt.show()
