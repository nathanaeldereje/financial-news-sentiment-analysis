from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
from scripts.utils import clean_text
import pandas as pd

def run_topic_modeling(df, n_topics=20):
    """
    Perform NMF topic modeling on cleaned headlines.

    Parameters
    ----------
    df : DataFrame
        Must contain 'clean_headline'
    n_topics : int
        Number of topics to extract
    top_n : int
        Number of keywords per topic

    Returns
    -------
    list
        A list of topics, each containing a list of words
    """

    
    vectorizer = TfidfVectorizer(ngram_range=(1,3), min_df=10, max_df=0.5, max_features=200_000)
    X = vectorizer.fit_transform(df['clean_headline'])
    
    nmf = NMF(n_components=n_topics, random_state=42, init='nndsvd')
    nmf.fit(X)
    
    for idx, topic in enumerate(nmf.components_):
        words = [vectorizer.get_feature_names_out()[i] for i in topic.argsort()[:-16:-1]]
        print(f"Topic {idx}: {' | '.join(words)}")


def extract_keywords(df, top_n=30):
    """
    Extract top TF-IDF keywords from cleaned headlines.

    Parameters
    ----------
    df : DataFrame
        Must contain a column 'clean_headline'
    top_n : int
        Number of top keywords to return

    Returns
    -------
    DataFrame
        Top keywords with TF-IDF scores
    """

    df['clean_headline'] = df['headline'].apply(clean_text)
    tfidf = TfidfVectorizer(
        ngram_range=(1, 3),
        min_df=5,
        max_df=0.7,
        stop_words='english'
    )
    
    X_tfidf = tfidf.fit_transform(df['clean_headline'])
    
    scores = pd.DataFrame(
        X_tfidf.sum(axis=0).A1,
        index=tfidf.get_feature_names_out(),
        columns=['tfidf_sum']
    ).sort_values('tfidf_sum', ascending=False)
    
    return scores.head(top_n)
