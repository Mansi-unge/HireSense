from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match_score(resume_text, jd_text):
    """
    Calculates similarity score between resume and job description
    using TF-IDF and cosine similarity.
    """
    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors)[0][1]

    return round(similarity * 100, 2)
