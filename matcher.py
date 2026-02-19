from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match_score(resume_text, jd_text):
    """
    Calculates the similarity between a resume and a job description using TF-IDF and cosine similarity.

    Parameters:
        resume_text (str): Preprocessed text content of the resume.
        jd_text (str): Preprocessed text content of the job description.

    Returns:
        float: Similarity score as a percentage (0-100), where higher values indicate better match.
    """

    # 1. Initialize TF-IDF vectorizer
    # TF-IDF converts text into numerical feature vectors based on term frequency and inverse document frequency
    vectorizer = TfidfVectorizer()

    # 2. Fit the vectorizer on both texts and transform them into vectors
    # The result is a sparse matrix representing each text in high-dimensional space
    vectors = vectorizer.fit_transform([resume_text, jd_text])

    # 3. Compute cosine similarity between the two vectors
    # Cosine similarity measures the cosine of the angle between two vectors (1 = identical, 0 = completely different)
    similarity = cosine_similarity(vectors)[0][1]

    # 4. Convert similarity to percentage for easier interpretation
    return similarity * 100
