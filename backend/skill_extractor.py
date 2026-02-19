def load_skills(file_path):
    """
    Loads a list of skills from a text file.

    Parameters:
        file_path (str): Path to the skills file (one skill per line).

    Returns:
        list: A list of skills in lowercase.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        # Strip whitespace and convert to lowercase for consistency
        return [line.strip().lower() for line in file if line.strip()]


def extract_skills(text, skills_list):
    """
    Extracts the skills present in the given text based on a predefined skills list.

    Parameters:
        text (str): Text to analyze (e.g., resume or job description).
        skills_list (list): List of known skills to look for.

    Returns:
        list: List of matched skills (no duplicates).
    """
    text_lower = text.lower()  # Ensure text is lowercase for matching
    matched_skills = [skill for skill in skills_list if skill in text_lower]
    
    # Return unique skills only
    return list(set(matched_skills))
