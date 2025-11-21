import string
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

# Pre-compute for speed
stop_words = set(stopwords.words('english'))
stemmer = SnowballStemmer("english")
translator = str.maketrans('', '', string.punctuation + '“”"\'‘’')

def clean_text(text: str) -> str:
    """
    Clean and stem headline text for NLP analysis.
    
    Steps:
    - Lowercase
    - Remove punctuation
    - Remove stopwords
    - Snowball stemming
    
    Parameters
    ----------
    text : str
    
    Returns
    -------
    str : cleaned and stemmed text
    """
    if not isinstance(text, str):
        return ""
    text = text.lower().translate(translator)
    words = [stemmer.stem(w) for w in text.split() if w not in stop_words]
    return " ".join(words)