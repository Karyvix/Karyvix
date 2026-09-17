# Karyvix — AI Career Intelligence Platform

Karyvix is an AI-powered career intelligence platform designed to help users understand their career fit, identify skill gaps, and make better career decisions.

> Understand your career. Discover your potential. Execute your next move.

## Overview

Karyvix analyzes career-related information using AI to provide actionable insights around:

* **Resume quality** — Structural evaluation and improvement metrics.
* **Job matching** — Contextual fit analysis between candidate and role.
* **Career analysis** — High-level career readiness mapping.
* **Skill gaps** — Technical and non-technical gap detection.
* **Recommendations** — Custom actionable roadmaps for career development.

The project is being developed incrementally as a full-stack AI application.

## Current Features

### Resume Parsing
Extracts structured information from uploaded resumes for downstream analysis.

### AI Job Matching
Analyzes the relationship between a candidate's profile and a target job description.

### Resume Quality Analysis
Evaluates resume quality and identifies precise areas that can be improved.

### Career Analysis
Combines AI-driven career analysis with resume quality insights to provide a broader view of career readiness.

## Technology Stack

### Backend
* **Python**
* **FastAPI**
* **Pydantic**
* **Google Gemini API**

### AI / Data
* **Google Gemini Models**
* **Resume parsing and analysis pipelines**

### Frontend
* **React**
* **Vite**
* **JavaScript / JSX**
* **Lucide React** (Icons)

### Development & DevOps
* **Git**
* **GitHub**

## Project Structure

```text
Karyvix/
├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│   └── main.py
├── frontend/
│   ├── public/
│   └── src/
├── tests/
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```
