
# =========================================
# RESUME JOB MATCHER
# =========================================

from flask import Flask, render_template, request
import pdfplumber
import re
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from collections import Counter

app = Flask(__name__)

# Load NLP model once at startup
model = SentenceTransformer("all-MiniLM-L6-v2")

SKILLS = [
    "python","java","c++","sql","html","css","javascript",
    "git","github","flask","machine learning","firebase",
    "flutter","arduino","esp32","iot","vivado","fpga",
    "embedded systems","linux","docker","aws"
]

DOMAIN_KEYWORDS = {
    "Embedded Systems": ["arduino","esp32","embedded","firmware","real-time"],
    "IoT Development": ["iot","sensor","monitoring","esp32"],
    "FPGA Development": ["fpga","vivado","verilog","waveform"],
    "Web Development": ["html","css","javascript","flask"],
    "Mobile Development": ["flutter","android"],
    "Machine Learning": ["machine learning","prediction","analysis"],
    "Research & Development": ["research","testing","documentation"]
}

CAREER_PATHS = {
    "Embedded Systems Engineer": ["arduino","esp32","embedded","fpga","vivado","sensor"],
    "IoT Engineer": ["iot","esp32","monitoring","sensor"],
    "Software Developer": ["python","html","css","javascript","flask"],
    "Research Engineer": ["research","analysis","testing","documentation"]
}

@app.route("/")
def home():
    return render_template(
        "index.html",
        skill_categories={},
        top_careers=[],
        sections=[],
        candidate_profile=[],
        detected_domains=[],
        summary=[],
        matched_areas=[],
        strengths=[],
        recommendations=[]
    )

@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["resume"]
    job_description = request.form["job_description"]

    resume_text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                resume_text += text + "\n"

    resume_lower = resume_text.lower()
    job_lower = job_description.lower()

    # Skill Detection
    resume_skills = [s for s in SKILLS if re.search(r"\b" + re.escape(s) + r"\b", resume_lower)]
    job_skills = [s for s in SKILLS if re.search(r"\b" + re.escape(s) + r"\b", job_lower)]

    matching_skills = list(set(resume_skills) & set(job_skills))
    missing_skills = list(set(job_skills) - set(resume_skills))

    # Skill Categories
    skill_categories = {
        "Embedded Systems": [],
        "Software Development": [],
        "Cloud & DevOps": [],
        "Machine Learning": []
    }

    for skill in resume_skills:
        if skill in ["arduino","esp32","iot","fpga","vivado","embedded systems"]:
            skill_categories["Embedded Systems"].append(skill)
        elif skill in ["python","html","css","javascript","flask","java"]:
            skill_categories["Software Development"].append(skill)
        elif skill in ["aws","docker","linux"]:
            skill_categories["Cloud & DevOps"].append(skill)
        elif skill == "machine learning":
            skill_categories["Machine Learning"].append(skill)

    # Domain Detection
    detected_domains = []
    for domain, keywords in DOMAIN_KEYWORDS.items():
        hits = sum(1 for keyword in keywords if keyword in resume_lower)
        if hits >= 2:
            detected_domains.append(domain)

    domain_count = len(detected_domains)

    # Career Prediction
    career_scores = {}
    for career, keywords in CAREER_PATHS.items():
        career_scores[career] = sum(1 for keyword in keywords if keyword in resume_lower)

    sorted_careers = sorted(career_scores.items(), key=lambda x: x[1], reverse=True)
    predicted_career = sorted_careers[0][0]
    top_careers = [c for c, _ in sorted_careers[:5]]

    career_confidence = round(
        (career_scores[predicted_career] / max(sum(career_scores.values()), 1)) * 100
    )

    # Resume Summary
    summary = []

    if "arduino" in resume_lower:
        summary.append("Experience with Arduino development.")
    if "esp32" in resume_lower:
        summary.append("Experience with ESP32 development.")
    if "fpga" in resume_lower:
        summary.append("Knowledge of FPGA design and simulation.")
    if "iot" in resume_lower:
        summary.append("Experience building IoT systems.")
    if "research" in resume_lower:
        summary.append("Research and technical documentation experience.")

    # Use actual resume content for semantic matching
    # This improves matching accuracy because the model
    # sees the real resume instead of a short summary.

    candidate_profile_text = resume_text[:5000]

    # Semantic Matching
    resume_embedding = model.encode(candidate_profile_text)
    job_embedding = model.encode(job_description)

    similarity = cosine_similarity(
        [resume_embedding],
        [job_embedding]
    )

    raw_score = similarity[0][0]

    # Scale semantic similarity to a more realistic recruiter score

    match_score = round(raw_score * 130)

    if match_score > 100:
        match_score = 100

    semantic_score = match_score

    skills_match_score = 0
    if len(job_skills) > 0:
        skills_match_score = round((len(matching_skills) / len(job_skills)) * 100)

    # Match Rating
    if match_score >= 90:
        match_rating = "Excellent Match"
    elif match_score >= 75:
        match_rating = "Strong Match"
    elif match_score >= 60:
        match_rating = "Good Match"
    elif match_score >= 40:
        match_rating = "Moderate Match"
    else:
        match_rating = "Weak Match"

    # Keywords
    stop_words = set(stopwords.words("english"))
    words = []

    for word in resume_lower.split():
        cleaned = re.sub(r"[^a-zA-Z]", "", word)
        if cleaned and cleaned not in stop_words and len(cleaned) > 3:
            words.append(cleaned)

    top_keywords = [w for w, _ in Counter(words).most_common(15)]

    # Statistics
    word_count = len(resume_text.split())
    skills_count = len(resume_skills)

    # Sections
    sections = []
    for section in ["education", "experience", "project", "leadership", "skill"]:
        if section in resume_lower:
            sections.append(section.title())

   # Resume quality scoring

    quality_score = 0

    # Resume sections
    quality_score += len(sections) * 10

    # Technical domains
    quality_score += len(detected_domains) * 5

    # Technical skills
    quality_score += min(len(resume_skills) * 2, 20)

    # Resume length

    if word_count >= 300:
        quality_score += 15
    elif word_count >= 200:
        quality_score += 10
    elif word_count >= 100:
        quality_score += 5

    quality_score = min(quality_score, 100)

    ats_score = 0
    ats_score += len(sections) * 10
    ats_score += min(len(resume_skills) * 2, 20)

    if "project" in resume_lower:
        ats_score += 20
    if "experience" in resume_lower:
        ats_score += 20
    if "education" in resume_lower:
        ats_score += 15
    if "leadership" in resume_lower:
        ats_score += 15

    ats_score = min(ats_score, 100)

    # Resume Grade

    if quality_score >= 95:
        resume_grade = "A+"
    elif quality_score >= 90:
        resume_grade = "A"
    elif quality_score >= 80:
        resume_grade = "B"
    elif quality_score >= 70:
        resume_grade = "C"
    else:
        resume_grade = "D"

    # Hiring Recommendation

    overall_score = round(
        (match_score * 0.5) +
        (ats_score * 0.25) +
        (quality_score * 0.25))

    if overall_score >= 90:
        hiring_recommendation = "Strongly Recommended"
    elif overall_score >= 75:
        hiring_recommendation = "Recommended"
    elif overall_score >= 60:
        hiring_recommendation = "Consider for Interview"
    else:
        hiring_recommendation = "Needs Improvement"

    matched_areas = []
    strengths = []
    # Generate recommendations based on missing skills
    recommendations = [
        f"Develop experience in {s}."
        for s in missing_skills
    ]

    # If resume already matches well, provide positive feedback
    if not recommendations:
        recommendations.append(
            "Your resume aligns well with the job requirements."
        )

    return render_template(
        "index.html",
        match_score=match_score,
        match_rating=match_rating,
        quality_score=quality_score,
        ats_score=ats_score,
        resume_skills=resume_skills,
        matching_skills=matching_skills,
        missing_skills=missing_skills,
        top_keywords=top_keywords,
        strengths=strengths,
        recommendations=recommendations,
        resume_text=resume_text,
        detected_domains=detected_domains,
        predicted_career=predicted_career,
        career_confidence=career_confidence,
        summary=summary,
        matched_areas=matched_areas,
        sections=sections,
        candidate_profile=[
            predicted_career,
            f"{skills_count} skills detected",
            f"{domain_count} domains detected",
            f"{career_confidence}% confidence"
        ],
        word_count=word_count,
        skills_count=skills_count,
        domain_count=domain_count,
        semantic_score=semantic_score,
        resume_grade=resume_grade,
        hiring_recommendation=hiring_recommendation,
        skills_match_score=skills_match_score,
        top_careers=top_careers,
        skill_categories=skill_categories
    )

if __name__ == "__main__":
    app.run(debug=True)
