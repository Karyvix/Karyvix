from app.services.ai_analyzer import analyze_resume


resume = """
Rishab Singh

Education:
B.Tech Computer Science and Engineering

Skills:
Python
C++
TensorFlow
OpenCV
FastAPI

Projects:
Built a face recognition system using Python, OpenCV and TensorFlow.
Developed a plant disease detection system using deep learning.
"""


job_description = """
AI/ML Software Engineering Intern

We are looking for a candidate with experience in Python,
machine learning, REST APIs and FastAPI.

Required:
Python
Machine Learning
FastAPI
SQL
Docker

Preferred:
AWS
TensorFlow
Computer Vision
"""


result = analyze_resume(
    resume,
    job_description
)


print("Match Score:", result.match_score)

print("\nMatched Skills:")
for skill in result.matched_skills:
    print("-", skill)

print("\nMissing Skills:")
for skill in result.missing_skills:
    print("-", skill)

print("\nStrengths:")
for strength in result.strengths:
    print("-", strength)

print("\nWeaknesses:")
for weakness in result.weaknesses:
    print("-", weakness)

print("\nRecommendations:")
for recommendation in result.recommendations:
    print("-", recommendation)