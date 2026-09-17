from unittest.mock import patch

from app.models.ai_analysis import AIAnalysis
from app.services.ai_analyzer import analyze_resume


def test_analyze_resume():
    fake_result = AIAnalysis(
        match_score=75,
        matched_skills=["Python", "FastAPI", "TensorFlow"],
        missing_skills=["SQL", "Docker", "AWS"],
        strengths=["Strong Python and AI/ML project experience."],
        weaknesses=["Limited cloud and containerization experience."],
        recommendations=["Learn Docker and AWS."],
    )

    fake_response = type(
        "FakeResponse",
        (),
        {
            "parsed": fake_result,
            "text": "",
        },
    )()

    with patch("app.services.ai_analyzer.genai.Client") as mock_client:
        mock_client.return_value.models.generate_content.return_value = (
            fake_response
        )

        result = analyze_resume(
            "Python FastAPI TensorFlow resume",
            "Python FastAPI SQL Docker AWS job",
        )

    assert isinstance(result, AIAnalysis)
    assert result.match_score == 75
    assert "Python" in result.matched_skills
    assert "FastAPI" in result.matched_skills
    assert "SQL" in result.missing_skills
    assert "Docker" in result.missing_skills
    assert "AWS" in result.missing_skills
