# Resume Job Matcher

Resume Job Matcher is an AI-powered web application that analyzes resumes and compares them against job descriptions using Natural Language Processing and semantic similarity techniques. The system helps job seekers evaluate how well their resume aligns with a target role while providing actionable feedback for improvement.

## Overview

This project combines resume parsing, skill extraction, semantic matching, ATS analysis, and career path prediction into a single platform. Users can upload a PDF resume, paste a job description, and receive detailed insights about their compatibility with the role.

The project was developed as part of a Computer Engineering portfolio focused on Artificial Intelligence, Machine Learning, Software Development, and Intelligent Decision Support Systems.

## Features

### Resume Analysis

* PDF resume upload and parsing
* Resume text extraction using PDFPlumber
* Resume statistics and keyword analysis
* Resume quality assessment
* Resume grading system

### Job Matching

* Semantic similarity matching using Sentence Transformers
* Match score calculation
* Match rating generation
* Skill matching analysis
* Missing skills identification

### ATS Evaluation

* ATS compatibility scoring
* Resume structure evaluation
* Section detection and analysis

### Career Intelligence

* Career path prediction
* Technical domain detection
* Candidate profile generation
* Career confidence scoring

### Recommendations

* Personalized resume recommendations
* Skill gap analysis
* Resume improvement suggestions
* Hiring recommendation system

### User Experience

* Dark mode and light mode support
* Custom resume upload interface
* Responsive design
* Interactive analysis dashboard

## Technologies Used

### Backend

* Python
* Flask
* Sentence Transformers
* Scikit-Learn
* NLTK
* PDFPlumber

### Frontend

* HTML
* CSS
* JavaScript

### Machine Learning and NLP

* all-MiniLM-L6-v2 Sentence Transformer
* Cosine Similarity
* Skill Extraction
* Semantic Matching
* Text Processing

## Project Structure

```text
resume-job-matcher/

├── app.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── main.js
│
├── uploads/
│
├── requirements.txt
│
└── README.md
```

## How It Works

1. Upload a PDF resume.
2. Paste a target job description.
3. The system extracts and processes resume content.
4. Skills and technical domains are identified.
5. Semantic similarity is calculated using Sentence Transformers.
6. ATS and quality scores are generated.
7. Career predictions and recommendations are produced.
8. Results are displayed through an interactive dashboard.

## Sample Outputs

* Match Score
* Match Rating
* ATS Compatibility Score
* Resume Quality Score
* Resume Grade
* Hiring Recommendation
* Predicted Career Path
* Technical Domains
* Matching Skills
* Missing Skills
* Resume Recommendations

## Future Improvements

* Interactive charts and analytics
* Drag-and-drop resume upload
* PDF report export
* Multi-resume comparison
* Resume history tracking
* Recruiter dashboard
* Advanced ATS analysis
* Cloud deployment

## Author

Mico H. Yumul

Bachelor of Science in Computer Engineering

Pampanga State University

## License

This project is intended for educational, research, and portfolio purposes.
