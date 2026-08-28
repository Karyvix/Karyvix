from fastapi import APIRouter

from app.models.matching import MatchRequest
from app.services.matcher import calculate_match_score


router = APIRouter(
    prefix="/match",
    tags=["Matching"]
)


SKILLS = [
    "Python",
    "C++",
    "Java",
    "JavaScript",
    "FastAPI",
    "Django",
    "Flask",
    "SQL",
    "MySQL",
    "PostgreSQL",
    "MongoDB",
    "Docker",
    "AWS",
    "Azure",
    "Git",
    "GitHub",
    "TensorFlow",
    "PyTorch",
    "OpenCV",
    "Machine Learning",
    "Deep Learning",
    "NLP",
    "REST APIs"
]


@router.post("/")
def match_resume(request: MatchRequest):

    result = calculate_match_score(
        request.resume_text,
        request.job_description,
        SKILLS
    )

    return result