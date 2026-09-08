from pydantic import BaseModel, Field


class ResumeQuality(BaseModel):
    overall_score: int = Field(
        description="Overall resume quality score from 0 to 100."
    )

    structure_score: int = Field(
        description="Score for resume organization and readability from 0 to 100."
    )

    skills_score: int = Field(
        description="Score for clarity and relevance of the skills section from 0 to 100."
    )

    projects_score: int = Field(
        description="Score for quality and relevance of projects from 0 to 100."
    )

    impact_score: int = Field(
        description="Score for measurable achievements and demonstrated impact from 0 to 100."
    )

    completeness_score: int = Field(
        description="Score for completeness of important resume information from 0 to 100."
    )

    strengths: list[str] = Field(
        description="Strong aspects of the resume."
    )

    weaknesses: list[str] = Field(
        description="Areas that weaken the resume."
    )

    recommendations: list[str] = Field(
        description="Specific actionable improvements."
    )