from pydantic import BaseModel, Field


class AIAnalysis(BaseModel):
    match_score: int = Field(
        description="Overall resume-to-job match score from 0 to 100."
    )

    matched_skills: list[str] = Field(
        description="Skills from the job description that the candidate demonstrates."
    )

    missing_skills: list[str] = Field(
        description="Important job skills that are missing or not clearly demonstrated in the resume."
    )

    strengths: list[str] = Field(
        description="The candidate's strongest qualifications for this specific job."
    )

    weaknesses: list[str] = Field(
        description="The most important gaps or weaknesses relative to this job."
    )

    recommendations: list[str] = Field(
        description="Specific actionable recommendations to improve the candidate's fit."
    )
class AIAnalysisRequest(BaseModel):
    resume_text: str
    job_description: str
class ResumeAnalysisRequest(BaseModel):
    job_description: str