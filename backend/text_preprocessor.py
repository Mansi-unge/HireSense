import spacy

# Load the small English model from spaCy
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    """
    Preprocesses input text using spaCy.

    Steps:
    1. Tokenize the text.
    2. Convert tokens to lowercase.
    3. Lemmatize tokens (convert to base form).
    4. Remove stop words and non-alphabetic tokens.

    Parameters:
        text (str): The input text (resume or job description).

    Returns:
        str: A cleaned and preprocessed version of the text.
    """
    # Process the text with spaCy NLP pipeline
    doc = nlp(text)

    # Keep only meaningful words: alphabetic, not stopwords, lemmatized
    cleaned_tokens = [
        token.lemma_.lower()
        for token in doc
        if token.is_alpha and not token.is_stop
    ]

    # Join tokens back into a single string
    return " ".join(cleaned_tokens)
