from resume_parser import extract_resume_text
from text_preprocessor import preprocess_text
from matcher import calculate_match_score

resume_text = preprocess_text(
    extract_resume_text("uploads/resumes/Mansi_Unge_Resume.pdf")
)

job_description = """
Looking for a Python developer with experience in Flask, REST APIs,
Docker, SQL databases, and Git. Knowledge of React is a plus.
"""

jd_text = preprocess_text(job_description)

score = calculate_match_score(resume_text, jd_text)

print("Match Score:", score, "%")
