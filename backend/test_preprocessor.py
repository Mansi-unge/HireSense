from resume_parser import extract_resume_text
from text_preprocessor import preprocess_text

raw_text = extract_resume_text("uploads/resumes/Mansi_Unge_Resume.pdf")
clean_text = preprocess_text(raw_text)

print("RAW TEXT SAMPLE:\n", raw_text[:300])
print("\nCLEANED TEXT SAMPLE:\n", clean_text[:300])
