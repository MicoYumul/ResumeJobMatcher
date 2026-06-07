# Resume Job Matcher & ATS Analyzer

An AI-powered recruitment analytics platform that evaluates resumes against job descriptions using Natural Language Processing (NLP), semantic similarity analysis, ATS scoring, and career intelligence.

## Overview

Resume Job Matcher helps job seekers, recruiters, and hiring teams assess candidate suitability by comparing resumes with job requirements. The platform provides detailed insights including match scores, ATS compatibility, skill gap analysis, career predictions, and hiring recommendations through an interactive analytics dashboard.
=======
An AI-powered Resume Job Matcher and ATS Analyzer built with Flask, NLP, Machine Learning, and Semantic Similarity techniques.

This application helps job seekers evaluate how well their resume aligns with a target job description by providing ATS analysis, semantic matching, skill gap detection, career insights, and professional reporting.
>>>>>>> 175a4a0 (Release v1.0 Resume Job Matcher ATS Analyzer)

## Features

### Resume Analysis

* PDF resume upload and processing
* Resume text extraction
* Resume preview viewer
* Resume quality assessment
* Resume grading system

### AI-Powered Job Matching

* Semantic similarity matching
* Match score calculation
* Candidate suitability evaluation
* Job description analysis
* Hiring recommendation generation

### ATS Analyzer

* ATS compatibility scoring
* Resume structure evaluation
* Keyword matching analysis
* Resume quality scoring

### Skills Intelligence

* Technical skill extraction
* Matching skills detection
* Missing skills identification
* Skill gap analysis
* Personalized recommendations
=======
* PDF Resume Upload
* Resume Text Extraction
* Resume Quality Analysis
* Resume Quality Scoring
* Resume Grading System
* Hiring Recommendation Engine
* Resume Preview

### ATS Analysis

* ATS Compatibility Scoring
* Keyword Analysis
* Resume Optimization Insights
* ATS Readiness Evaluation

### AI-Powered Matching

* Semantic Job Matching
* NLP-Based Similarity Analysis
* Job Skill Match Scoring
* Skill Gap Analysis
* Missing Skills Detection
* Matching Skills Detection
>>>>>>> 175a4a0 (Release v1.0 Resume Job Matcher ATS Analyzer)

### Career Intelligence

* Career Path Prediction
* Career Confidence Scoring
* Technical Domain Detection
* Candidate Profile Generation
* Skills Categorization

### Analytics Dashboard

* Match Score visualization
* ATS Score visualization
* Resume Quality visualization
* Interactive charts
* Progress indicators
* Candidate insights dashboard

### History Management

* SQLite database integration
* Analysis history storage
* Historical analysis dashboard
* Analysis record deletion
* Sortable score tables
* Performance statistics
=======
* Match Score Visualization
* ATS Score Visualization
* Resume Quality Visualization
* Resume Grade Display
* Hiring Recommendation Dashboard
* Skills Analysis Charts
* Career Analytics Dashboard

### History & Reporting

* Analysis History Storage
* Analysis Statistics Dashboard
* Sortable Analysis Records
* Professional PDF Report Export
* Session-Based Dashboard Persistence
>>>>>>> 175a4a0 (Release v1.0 Resume Job Matcher ATS Analyzer)

### Reporting

* Professional PDF report generation
* Downloadable analysis reports
* Candidate evaluation summaries

## Technology Stack

### Backend

* Python
* Flask
* SQLite

### Machine Learning & NLP

* Sentence Transformers
* Scikit-learn
* Natural Language Processing
* Cosine Similarity Analysis
=======
* Semantic Similarity Matching
>>>>>>> 175a4a0 (Release v1.0 Resume Job Matcher ATS Analyzer)

### Frontend

* HTML5
* CSS3
* JavaScript

* Jinja2 Templates

### Data Visualization

* Chart.js
=======
* Chart.js

### Database

* SQLite
>>>>>>> 175a4a0 (Release v1.0 Resume Job Matcher ATS Analyzer)

### Document Processing

* PDFPlumber
* ReportLab

## System Architecture

```text

Resume PDF
     │
     ▼
Text Extraction
     │
     ▼
Resume Analysis Engine
     │
     ├── Semantic Matching
     ├── ATS Scoring
     ├── Skill Detection
     ├── Career Prediction
     └── Resume Quality Assessment
     │
     ▼
Analytics Dashboard
     │
     ├── Match Score
     ├── ATS Score
     ├── Skill Gap Analysis
     ├── Career Intelligence
     └── PDF Reports
```

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/resume-job-matcher.git
cd resume-job-matcher
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Project Highlights

* AI-powered resume screening
* Semantic job matching engine
* ATS compatibility analysis
* Career prediction system
* Interactive analytics dashboard
* Historical analysis tracking
* PDF report generation
* Recruiter-focused evaluation workflow

## Future Enhancements

* Multi-resume comparison
* Advanced recommendation engine
* Candidate ranking dashboard
* Historical trend analytics
* User authentication
* Cloud deployment
* Recruiter management portal
* AI Resume Assistant

## Learning Outcomes

This project demonstrates practical experience in:

* Full Stack Web Development
* Machine Learning Integration
* Natural Language Processing
* Database Management
* Data Visualization
* Software Architecture Design
* Recruitment Technology Solutions

## Author

Mico Yumul

Computer Engineering Graduate

Passionate about Software Development, Artificial Intelligence, Embedded Systems, IoT, and Data-Driven Solutions.
=======
resume-job-matcher/
│
├── app.py
├── database.py
├── pdf_export.py
├── resume_history.db
│
├── analyzers/
│   ├── ats_analyzer.py
│   ├── career_predictor.py
│   ├── job_gap_analyzer.py
│   ├── resume_analyzer.py
│   └── semantic_matcher.py
│
├── reports/
│
├── templates/
│   ├── index.html
│   └── history.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── main.js
│
└── README.md
```

## Key Metrics Generated

### Resume Analysis Metrics

* Match Score
* ATS Score
* Resume Quality Score
* Semantic Similarity Score
* Resume Grade
* Hiring Recommendation

### Job Matching Metrics

* Job Skill Match Score
* Matching Skills
* Missing Skills
* Skill Gap Recommendations

### Career Metrics

* Predicted Career Path
* Career Confidence
* Technical Domains Detected
* Skills Count
* Domain Count

## Dashboard Overview

The dashboard provides:

* Resume Analysis Summary
* Candidate Profile
* Career Intelligence
* Analytics Dashboard
* Skills Analysis
* Job Gap Analysis
* Resume Preview
* Downloadable PDF Reports

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/resume-job-matcher.git
cd resume-job-matcher
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

## Sample Workflow

1. Upload a PDF Resume
2. Paste a Job Description
3. Run Analysis
4. Review ATS and Match Scores
5. Analyze Skill Gaps
6. Explore Career Insights
7. Download Professional PDF Report
8. View Analysis History

## Future Enhancements

* Resume Comparison Tool
* Multi-Resume Benchmarking
* Job Application Tracker
* Resume Version Management
* Cloud Deployment
* User Authentication

## Author

Developed by Mico Yumul

Computer Engineering Graduate

Focused on Software Development, Artificial Intelligence, Embedded Systems, IoT, and Data Analytics.

## License

This project is intended for educational, research, and portfolio purposes.
>>>>>>> 175a4a0 (Release v1.0 Resume Job Matcher ATS Analyzer)
