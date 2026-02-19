from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

# Import custom modules for resume analysis
from resume_parser import extract_resume_text
from text_preprocessor import preprocess_text
from skill_extractor import load_skills, extract_skills
from matcher import calculate_match_score

# ---------------- FLASK APP INITIALIZATION ----------------
app = Flask(__name__)

# ---------------- CONFIGURATION ----------------
# Folder to save uploaded resumes
UPLOAD_FOLDER = "uploads/resumes"
# Allowed file types
ALLOWED_EXTENSIONS = {"pdf", "docx"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ---------------- HELPER FUNCTIONS ----------------
def allowed_file(filename):
    """
    Check if the uploaded file has an allowed extension (pdf or docx).
    """
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# Predefined suggestions for missing skills
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
    """
    Main route for the HireSense resume analyzer.
    Handles both GET and POST requests.
    GET: Renders the homepage with resume upload form.
    POST: Processes uploaded resume, extracts skills, compares with job description,
          calculates match score, and provides suggestions.
    """
    if request.method == "POST":

        # ---------------- VALIDATE FILE UPLOAD ----------------
        if "resume" not in request.files:
            return "No file uploaded"

        resume_file = request.files["resume"]
        job_description = request.form.get("job_description", "")
        job_role = request.form.get("job_role", "")

        if resume_file.filename == "":
            return "No selected file"

        if not allowed_file(resume_file.filename):
            return "Invalid file type. Upload PDF or DOCX only."

        # ---------------- SAVE UPLOADED FILE ----------------
        filename = secure_filename(resume_file.filename)
        resume_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        resume_file.save(resume_path)

        # ---------------- EXTRACT RESUME TEXT ----------------
        raw_resume_text = extract_resume_text(resume_path)
        if not raw_resume_text.strip():
            return "Unable to read resume. Please upload a valid PDF or DOCX file."

        # ---------------- PREPROCESS TEXT ----------------
        # Clean and standardize text for comparison
        resume_text = preprocess_text(raw_resume_text)
        jd_text = preprocess_text(job_description)

        # ---------------- SKILL EXTRACTION ----------------
        # Load predefined skills list
        skills = load_skills("data/skills_list.txt")
        # Extract skills from resume and job description
        resume_skills = extract_skills(resume_text, skills)
        jd_skills = extract_skills(jd_text, skills)

        # ---------------- SKILL MATCHING ----------------
        match_score = calculate_match_score(resume_text, jd_text)
        missing_skills = list(set(jd_skills) - set(resume_skills))

        # Counts for dashboard display
        matched_count = len(resume_skills)
        missing_count = len(missing_skills)
        total_skills = len(jd_skills)

        # Categorize match based on score
        if match_score >= 70:
            match_category = "good"
        elif match_score >= 40:
            match_category = "average"
        else:
            match_category = "poor"

        # Create detailed skill breakdown for frontend display
        skill_breakdown = []
        for skill in jd_skills:
            skill_breakdown.append({
                "skill": skill,
                "in_resume": skill in resume_skills
            })

        # Generate improvement suggestions if match is low
        suggestions = []
        if match_score < 60:
            for skill in missing_skills:
                suggestions.append(
                    SUGGESTION_MAP.get(
                        skill.lower(),
                        f"Consider adding experience with {skill}."
                    )
                )

        # ---------------- RENDER RESULT TEMPLATE ----------------
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
            job_role=job_role
        )

    # Render homepage for GET requests
    return render_template("index.html")


# ---------------- RUN FLASK APP ----------------
if __name__ == "__main__":
    # Debug should be turned off in production
    app.run(debug=True)
