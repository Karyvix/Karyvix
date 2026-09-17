from unittest.mock import patch

from app.models.resume_quality import ResumeQuality
from app.services.resume_quality import analyze_resume_quality


def test_analyze_resume_quality():
    fake_result = ResumeQuality(
        overall_score=80,
        structure_score=85,
        skills_score=78,
        projects_score=82,
        impact_score=70,
        completeness_score=88,
        strengths=["Clear structure and relevant technical projects."],
        weaknesses=["Limited measurable project impact."],
        recommendations=["Add quantitative results to project descriptions."],
    )

    fake_response = type(
        "FakeResponse",
        (),
        {
            "parsed": fake_result,
            "text": "",
        },
    )()

    with patch("app.services.resume_quality.genai.Client") as mock_client:
        mock_client.return_value.models.generate_content.return_value = (
            fake_response
        )

        result = analyze_resume_quality(
            "Python FastAPI TensorFlow resume with AI/ML projects"
        )

    assert isinstance(result, ResumeQuality)
    assert result.overall_score == 80
    assert result.structure_score == 85
    assert result.skills_score == 78
    assert result.projects_score == 82
    assert result.impact_score == 70
    assert result.completeness_score == 88

    assert "Clear structure and relevant technical projects." in result.strengths
    assert "Limited measurable project impact." in result.weaknesses
    assert "Add quantitative results to project descriptions." in result.recommendations
