from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

from resume_parser import extract_resume_text
from text_preprocessor import preprocess_text
from skill_extractor import load_skills, extract_skills
from matcher import calculate_match_score

app = Flask(__name__)

# ---------------- CONFIG ----------------
UPLOAD_FOLDER = "uploads/resumes"
ALLOWED_EXTENSIONS = {"pdf", "docx"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# ---------------------------------------


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # 1. Validate file
        if "resume" not in request.files:
            return "No file uploaded"

        resume_file = request.files["resume"]
        job_description = request.form["job_description"]

        if resume_file.filename == "":
            return "No selected file"

        if not allowed_file(resume_file.filename):
            return "Invalid file type. Upload PDF or DOCX only."

        # 2. Secure filename & save
        filename = secure_filename(resume_file.filename)
        resume_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        resume_file.save(resume_path)

        # 3. Process resume & JD
        resume_text = preprocess_text(
            extract_resume_text(resume_path)
        )
        jd_text = preprocess_text(job_description)

        # 4. Skill extraction
        skills = load_skills("data/skills_list.txt")
        resume_skills = extract_skills(resume_text, skills)
        jd_skills = extract_skills(jd_text, skills)

        # 5. Matching
        match_score = calculate_match_score(resume_text, jd_text)
        missing_skills = list(set(jd_skills) - set(resume_skills))

        return render_template(
            "result.html",
            score=match_score,
            resume_skills=resume_skills,
            missing_skills=missing_skills
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
