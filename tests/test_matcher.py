from app.services.matcher import calculate_match_score


def test_match_score():
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
        "AWS",
    ]

    result = calculate_match_score(
        resume,
        job_description,
        skills,
    )

    assert result["score"] == 40.0
    assert "Python" in result["matched_skills"]
    assert "FastAPI" in result["matched_skills"]
    assert "SQL" in result["missing_skills"]
    assert "Docker" in result["missing_skills"]
    assert "AWS" in result["missing_skills"]
