# Resume Job Matcher & ATS Analyzer

An AI-powered recruitment analytics platform that evaluates resumes against job descriptions using Natural Language Processing (NLP), semantic similarity analysis, ATS scoring, and career intelligence.

## Overview

Resume Job Matcher helps job seekers, recruiters, and hiring teams assess candidate suitability by comparing resumes with job requirements. The platform provides detailed insights including match scores, ATS compatibility, skill gap analysis, career predictions, and hiring recommendations through an interactive analytics dashboard.

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

### Career Intelligence

* Career path prediction
* Technical domain detection
* Candidate profile generation
* Career confidence scoring

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

### Frontend

* HTML5
* CSS3
* JavaScript
* Jinja2 Templates

### Data Visualization

* Chart.js

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
