from pydantic import BaseModel, Field


class ResumeQuality(BaseModel):
    overall_score: int = Field(
        ge=0,
        le=100,
        description="Overall resume quality score from 0 to 100.",
    )

    structure_score: int = Field(
        ge=0,
        le=100,
        description="Resume structure score from 0 to 100.",
    )

    skills_score: int = Field(
        ge=0,
        le=100,
        description="Skills section quality score from 0 to 100.",
    )

    projects_score: int = Field(
        ge=0,
        le=100,
        description="Projects section quality score from 0 to 100.",
    )

    impact_score: int = Field(
        ge=0,
        le=100,
        description="Impact and achievement quality score from 0 to 100.",
    )

    completeness_score: int = Field(
        ge=0,
        le=100,
        description="Resume completeness score from 0 to 100.",
    )

    strengths: list[str] = Field(default_factory=list)
    weaknesses: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)