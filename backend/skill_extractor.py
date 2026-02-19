def load_skills(file_path):
    """
    Loads predefined skills from a text file
    """
    with open(file_path, "r") as file:
        skills = [line.strip().lower() for line in file]
    return skills


def extract_skills(text, skills_list):
    """
    Extracts skills present in text based on predefined skill list
    """
    extracted = []

    for skill in skills_list:
        if skill in text:
            extracted.append(skill)

    return list(set(extracted))
