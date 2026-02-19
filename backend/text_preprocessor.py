import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    """
    Cleans and preprocesses text using NLP.
    - Removes stopwords
    - Removes punctuation
    - Lemmatizes words
    """
    doc = nlp(text)

    cleaned_tokens = [
        token.lemma_.lower()
        for token in doc
        if token.is_alpha and not token.is_stop
    ]

    return " ".join(cleaned_tokens)
