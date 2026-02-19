import sqlite3
from datetime import datetime

DB_PATH = "db/analysis.db"

# Ensure the folder exists
import os
os.makedirs("db", exist_ok=True)

def create_table():
    """Create table to store resume analysis results if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS analysis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_role TEXT,
            resume_skills TEXT,
            missing_skills TEXT,
            skill_match_score REAL,
            content_similarity_score REAL,
            final_score REAL,
            analyzed_at TEXT
        )
    """)
    conn.commit()
    conn.close()


def save_analysis(job_role, resume_skills, missing_skills, skill_match_score, content_similarity_score, final_score):
    """Save the analysis results to the database."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        INSERT INTO analysis (
            job_role, resume_skills, missing_skills, skill_match_score, content_similarity_score, final_score, analyzed_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        job_role,
        ",".join(resume_skills),
        ",".join(missing_skills),
        skill_match_score,
        content_similarity_score,
        final_score,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


def get_last_5_analyses():
    """Fetch the last 5 analysis submissions from the database."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM analysis ORDER BY id DESC LIMIT 5")
    rows = c.fetchall()
    conn.close()
    return rows
