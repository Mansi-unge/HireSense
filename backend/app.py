from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from database import create_table, save_analysis, get_last_5_analyses

# Import custom modules for resume analysis
from resume_parser import extract_resume_text
from text_preprocessor import preprocess_text
from skill_extractor import load_skills, extract_skills
from matcher import calculate_match_score

# ---------------- FLASK APP INITIALIZATION ----------------
app = Flask(__name__)

# ---------------- CONFIGURATION ----------------
UPLOAD_FOLDER = "uploads/resumes"
ALLOWED_EXTENSIONS = {"pdf", "docx"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Create SQLite table if not exists
create_table()

# ---------------- HELPER FUNCTIONS ----------------
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

SUGGESTION_MAP = {
    "python": "Add more Python-based project experience.",
    "flask": "Mention Flask APIs and backend services you have built.",
    "nlp": "Include NLP concepts or libraries like spaCy or NLTK.",
    "scikit-learn": "Add machine learning projects using scikit-learn.",
    "docker": "Mention Docker-based deployments or containerization.",
    "mysql": "Include experience with relational databases like MySQL.",
    "mongodb": "Add NoSQL database usage like MongoDB.",
    "react": "Highlight frontend experience using React.js.",
    "javascript": "Mention strong JavaScript fundamentals."
}

# ---------------- MAIN ROUTE ----------------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Validate file
        if "resume" not in request.files:
            return "No file uploaded"
        resume_file = request.files["resume"]
        job_description = request.form.get("job_description", "")
        job_role = request.form.get("job_role", "")

        if resume_file.filename == "":
            return "No selected file"
        if not allowed_file(resume_file.filename):
            return "Invalid file type. Upload PDF or DOCX only."

        # Save uploaded file
        filename = secure_filename(resume_file.filename)
        resume_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        resume_file.save(resume_path)

        # Extract and preprocess text
        raw_resume_text = extract_resume_text(resume_path)
        if not raw_resume_text.strip():
            return "Unable to read resume. Please upload a valid PDF or DOCX file."
        resume_text = preprocess_text(raw_resume_text)
        jd_text = preprocess_text(job_description)

        # Extract skills
        skills = load_skills("data/skills_list.txt")
        resume_skills = extract_skills(resume_text, skills)
        jd_skills = extract_skills(jd_text, skills)

        # Calculate skill match
        match_score = calculate_match_score(resume_text, jd_text)
        missing_skills = list(set(jd_skills) - set(resume_skills))

        #  Corrected matched count & percentages
        matched_count = len(set(resume_skills) & set(jd_skills))
        missing_count = len(missing_skills)
        total_skills = len(jd_skills)

        # Categorize match
        if match_score >= 70:
            match_category = "good"
        elif match_score >= 40:
            match_category = "average"
        else:
            match_category = "poor"

        # Skill breakdown for frontend
        skill_breakdown = [{"skill": s, "in_resume": s in resume_skills} for s in jd_skills]

        # Suggestions
        suggestions = []
        if match_score < 60:
            for skill in missing_skills:
                suggestions.append(SUGGESTION_MAP.get(skill.lower(), f"Consider adding experience with {skill}."))

        # ---------------- Weighted final score ----------------
        skill_match_percentage = (matched_count / total_skills * 100) if jd_skills else 0
        content_similarity_percentage = match_score
        final_score = round(0.6 * skill_match_percentage + 0.4 * content_similarity_percentage, 2)

        # ---------------- Save analysis to SQLite ----------------
        save_analysis(
            job_role=job_role,
            resume_skills=resume_skills,
            missing_skills=missing_skills,
            skill_match_score=skill_match_percentage,
            content_similarity_score=content_similarity_percentage,
            final_score=final_score
        )

        # ---------------- Render result ----------------
        return render_template(
            "result.html",
            score=round(match_score, 2),
            resume_skills=resume_skills,
            missing_skills=missing_skills,
            match_category=match_category,
            skill_breakdown=skill_breakdown,
            suggestions=suggestions,
            matched_count=matched_count,
            missing_count=missing_count,
            total_skills=total_skills,
            job_role=job_role,
            skill_match_score=skill_match_percentage,
            content_similarity_score=content_similarity_percentage,
            final_score=final_score
        )

    return render_template("index.html")


# ---------------- DASHBOARD ROUTE ----------------
@app.route("/dashboard")
def dashboard():
    last_analyses = get_last_5_analyses()
    return render_template("dashboard.html", analyses=last_analyses)


# ---------------- RUN FLASK APP ----------------
if __name__ == "__main__":
    app.run(debug=True)
