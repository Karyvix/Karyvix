from pydantic import BaseModel, Field


class AIAnalysis(BaseModel):
    match_score: int = Field(
        ge=0,
        le=100,
        description="Job match score from 0 to 100.",
    )

    matched_skills: list[str] = Field(default_factory=list)
    missing_skills: list[str] = Field(default_factory=list)
    strengths: list[str] = Field(default_factory=list)
    weaknesses: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)


class AIAnalysisRequest(BaseModel):
    resume_text: str
    job_description: str


class ResumeAnalysisRequest(BaseModel):
    resume_text: str
    job_description: str