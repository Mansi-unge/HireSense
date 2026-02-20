#HireSense – AI Resume Analyzer & Skill Matcher

HireSense is an **AI-powered Resume Analyzer** built with **Flask** that compares a candidate’s resume against a **Job Description (JD)**, calculates a **match score**, highlights **matched & missing skills**, and provides **AI-driven improvement suggestions**.

> *Interview-ready feature:*  
> **“The system doesn’t just score resumes — it suggests how to improve them.”**

---

##Features

###Resume Parsing
- Supports **PDF** and **DOCX** resumes
- Extracts raw text from resumes automatically

###AI Skill Matching
- Compares resume content with job description
- Identifies **matched skills** and **missing skills**

###Match Score with Visual Feedback
- **🟢 70–100%** → Good Fit  
- **🟡 40–69%** → Partial Fit  
- **🔴 <40%** → Needs Improvement  

###Skill Match Breakdown
Clear table view:
| Skill | Resume | Job Description |
|------|--------|----------------|
| Python | ✅ | ✅ |
| NLP | ❌ | ✅ |

###AI Resume Improvement Suggestions
- Smart suggestions based on missing skills  
- Example:
  - *“Add experience with Flask APIs”*
  - *“Mention NLP libraries like spaCy”*

###Modern UI
- Built with **Bootstrap 5**
- Uses **Font Awesome icons**
- Clean, recruiter-friendly design

---

##Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, Bootstrap 5  
- **AI/NLP:** Text preprocessing & skill matching logic  
- **File Handling:** PDF & DOCX parsing  

---

##Project Structure

```text
HireSense/
│
├── app.py                     # Main Flask application
├── resume_parser.py           # Resume text extraction logic
├── text_preprocessor.py       # Cleaning & preprocessing text
├── skill_extractor.py         # Skill extraction logic
├── matcher.py                 # Match score calculation
│
├── data/
│   └── skills_list.txt        # List of skills (DevOps, NLP, etc.)
│
├── templates/
│   ├── index.html             # Upload form
│   └── result.html            # Analysis result page
│
├── uploads/
│   └── resumes/               # Uploaded resume files
│
├── requirements.txt
└── README.md
```

---

##Installation & Setup
Clone the Repository
git clone https://github.com/your-username/HireSense.git
cd HireSense
2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run the Application
python app.py
5️⃣ Open in Browser
http://127.0.0.1:5000

---

##How It Works

Upload a resume (PDF/DOCX)

Paste the Job Description

###System:
Extracts resume text
Preprocesses resume & JD
Matches skills
Calculates match percentage

###Displays:
Match score
Skill breakdown
Missing skills
AI improvement tips

---

##Use Cases

Students preparing for placements
Job seekers optimizing resumes
Recruiters doing quick resume screening
Resume ATS simulation projects
AI/NLP portfolio projects

---

##Future Enhancements
Resume scoring with NLP embeddings
JD-wise skill weighting
Resume PDF report download
Login system & history tracking
Cloud deployment (Render / AWS)

---

##Author
Mansi Unge
UI/UX Designer | Frontend & Full Stack Developer


---
