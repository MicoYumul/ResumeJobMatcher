# Resume Job Matcher & ATS Analyzer

An AI-powered Resume Job Matcher and ATS Analyzer built with Flask, Natural Language Processing, Machine Learning, and Semantic Similarity Analysis.

This application helps job seekers evaluate resume quality, measure compatibility with target job descriptions, identify skill gaps, and generate actionable recommendations through an interactive analytics dashboard.

## Features

### Resume Analysis

* PDF Resume Upload
* Resume Text Extraction
* Resume Preview
* Resume Quality Assessment
* Resume Quality Scoring
* Resume Grading System
* Hiring Recommendation Engine

### ATS Analysis

* ATS Compatibility Scoring
* Resume Optimization Insights
* Keyword Analysis
* ATS Readiness Evaluation

### AI Job Matching

* Semantic Job Matching
* NLP-Based Similarity Analysis
* Match Score Calculation
* Skill Gap Detection
* Matching Skills Identification
* Missing Skills Analysis
* Job Skill Match Score

### Career Intelligence

* Career Path Prediction
* Career Confidence Analysis
* Technical Domain Detection
* Candidate Profile Generation
* Skill Categorization

### Analytics Dashboard

* Match Score Visualization
* ATS Score Visualization
* Resume Quality Visualization
* Resume Grade Dashboard
* Hiring Recommendation Dashboard
* Career Intelligence Dashboard
* Skills Analysis Charts

### History & Reporting

* Analysis History Storage
* Analysis Statistics Dashboard
* Sortable Analysis Records
* PDF Report Export
* Session-Based Dashboard Persistence

## Technology Stack

### Backend

* Python
* Flask
* SQLite

### Machine Learning & NLP

* Sentence Transformers
* Scikit-learn
* Natural Language Processing
* Semantic Similarity Matching

### Frontend

* HTML5
* CSS3
* JavaScript
* Chart.js

### Database

* SQLite

## Project Architecture

```text
resume-job-matcher/
│
├── app.py
├── database.py
├── pdf_export.py
├── requirements.txt
│
├── analyzers/
│   ├── ats_analyzer.py
│   ├── career_predictor.py
│   ├── job_gap_analyzer.py
│   ├── resume_analyzer.py
│   └── semantic_matcher.py
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
├── reports/
│
└── README.md
```

## Key Metrics Generated

### Resume Metrics

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
* Career Confidence Score
* Technical Domains Detected
* Skills Count
* Domain Count

## Dashboard Modules

### Resume Analysis Dashboard

Provides an overview of:

* Match Score
* ATS Score
* Resume Quality Score
* Resume Grade
* Hiring Recommendation

### Career Intelligence

Provides:

* Predicted Career Path
* Career Confidence
* Skills Analysis
* Domain Analysis

### Job Gap Analysis

Provides:

* Job Skill Match Score
* Matching Skills
* Missing Skills
* Personalized Recommendations

### Analysis History

Provides:

* Historical Analysis Records
* Performance Statistics
* Score Tracking
* Sortable Results

## Installation

### Clone Repository

```bash
git clone https://github.com/MicoYumul/ResumeJobMatcher.git
cd ResumeJobMatcher
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

### Open in Browser

```text
http://127.0.0.1:5000
```

## Workflow

1. Upload a PDF Resume
2. Paste a Job Description
3. Run Resume Analysis
4. Review ATS and Match Scores
5. Analyze Skill Gaps
6. Review Career Insights
7. Download PDF Report
8. View Analysis History

## Screenshots

Add project screenshots here:

* Main Dashboard
* Analytics Dashboard
* Career Intelligence Section
* Job Gap Analysis
* Analysis History
* PDF Report

## Future Improvements

* Resume Comparison Tool
* Multi-Resume Benchmarking
* User Authentication
* Cloud Deployment
* Enhanced Reporting
* Additional NLP Models

## Author

Mico Yumul

Computer Engineering Graduate

Interests:

* Software Development
* Artificial Intelligence
* Machine Learning
* Embedded Systems
* Internet of Things (IoT)
* Data Analytics

## License

This project is released for educational, research, and portfolio purposes.
