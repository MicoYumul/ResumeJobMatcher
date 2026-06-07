# =========================================
# JOB GAP ANALYZER
# =========================================

import re

TECH_SKILLS = [
    "python",
    "java",
    "c++",
    "c#",
    "sql",
    "mysql",
    "postgresql",
    "sqlite",
    "html",
    "css",
    "javascript",
    "react",
    "nodejs",
    "flask",
    "django",
    "git",
    "github",
    "linux",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "firebase",
    "flutter",
    "arduino",
    "esp32",
    "iot",
    "machine learning",
    "artificial intelligence",
    "data analysis",
    "fpga",
    "vivado",
    "verilog",
    "embedded systems",
    "firmware",
    "rest api",
    "api",
    "jenkins",
    "ci/cd"
]


def extract_resume_skills(resume_text):
    """
    Extract technical skills found in the resume.
    """

    resume_lower = resume_text.lower()

    detected_skills = [
        skill
        for skill in TECH_SKILLS
        if re.search(r"\b" + re.escape(skill) + r"\b", resume_lower)
    ]

    return sorted(list(set(detected_skills)))


def extract_job_skills(job_description):
    """
    Extract technical skills found in the job description.
    """

    job_lower = job_description.lower()

    detected_skills = [
        skill
        for skill in TECH_SKILLS
        if re.search(r"\b" + re.escape(skill) + r"\b", job_lower)
    ]

    return sorted(list(set(detected_skills)))

def calculate_skill_match_score(resume_text, job_description):
    """
    Calculate percentage of required job skills
    found in the resume.
    """

    resume_skills = set(
        extract_resume_skills(resume_text)
    )

    job_skills = set(
        extract_job_skills(job_description)
    )

    if len(job_skills) == 0:
        return 100

    matched_skills = resume_skills.intersection(job_skills)

    score = round(
        (len(matched_skills) / len(job_skills)) * 100
    )

    return score


def get_job_gap_analysis(resume_text, job_description):
    """
    Complete job gap analysis.
    Returns everything needed for dashboard display.
    """

    resume_skills = extract_resume_skills(resume_text)

    job_skills = extract_job_skills(job_description)

    matching_skills = sorted(
        list(set(resume_skills) & set(job_skills))
    )

    missing_skills = sorted(
        list(set(job_skills) - set(resume_skills))
    )

    match_score = calculate_skill_match_score(
        resume_text,
        job_description
    )

    recommendations = []

    if missing_skills:

        recommendations.append(
            f"Focus on learning these missing skills: {', '.join(missing_skills[:5])}."
        )

        recommendations.append(
            "Add relevant projects that demonstrate the required technologies."
        )

        recommendations.append(
            "Highlight certifications, coursework, or practical experience related to the missing skills."
        )

    else:

        recommendations.append(
            "Your resume covers all detected job skills."
        )

    return {
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matching_skills": matching_skills,
        "missing_skills": missing_skills,
        "match_score": match_score,
        "recommendations": recommendations
    }