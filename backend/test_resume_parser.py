from resume_parser import extract_resume_text

text = extract_resume_text("uploads/resumes/Mansi_Unge_Resume.pdf")
print(text[:1000])   # print first 1000 characters
