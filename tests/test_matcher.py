from app.services.matcher import calculate_match_score


resume = """
Rishab Singh

Skills:
Python
C++
TensorFlow
OpenCV
FastAPI
"""


job_description = """
Python Developer

Required Skills:
Python
FastAPI
SQL
Docker
AWS
"""


skills = [
    "Python",
    "FastAPI",
    "SQL",
    "Docker",
    "AWS"
]


result = calculate_match_score(
    resume,
    job_description,
    skills
)


print("Match Score:", result["score"])
print("Matched Skills:", result["matched_skills"])
print("Missing Skills:", result["missing_skills"])