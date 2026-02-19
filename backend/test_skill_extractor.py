from resume_parser import extract_resume_text
from text_preprocessor import preprocess_text
from skill_extractor import load_skills, extract_skills

resume_text = extract_resume_text("uploads/resumes/Mansi_Unge_Resume.pdf")
clean_text = preprocess_text(resume_text)

skills_list = load_skills("data/skills_list.txt")
resume_skills = extract_skills(clean_text, skills_list)

print("Extracted Resume Skills:")
print(resume_skills)
