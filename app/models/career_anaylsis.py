from pydantic import BaseModel

from app.models.ai_analysis import AIAnalysis
from app.models.resume_quality import ResumeQuality


class CareerAnalysis(BaseModel):
    filename: str
    job_match: AIAnalysis
    resume_quality: ResumeQuality