def calculate_match_score(
    resume_text: str,
    job_description: str,
    skills: list[str]
) -> dict:
    """
    Calculate a basic resume-to-job skill match score.

    Args:
        resume_text: Extracted resume text.
        job_description: Cleaned job description.
        skills: List of skills to check.

    Returns:
        Matching skills, missing skills, and match percentage.
    """

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    required_skills = []

    for skill in skills:
        if skill.lower() in job_description:
            required_skills.append(skill)

    matched_skills = []

    for skill in required_skills:
        if skill.lower() in resume_text:
            matched_skills.append(skill)

    missing_skills = [
        skill for skill in required_skills
        if skill not in matched_skills
    ]

    if required_skills:
        score = (len(matched_skills) / len(required_skills)) * 100
    else:
        score = 0

    return {
        "score": round(score, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }