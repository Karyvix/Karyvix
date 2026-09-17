import os

from dotenv import load_dotenv
from google import genai

from app.models.resume_quality import ResumeQuality

load_dotenv()


def analyze_resume_quality(resume_text: str) -> ResumeQuality:
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not configured.")

    client = genai.Client(api_key=api_key)

    prompt = f"""
Evaluate the quality of the following resume.

RESUME:
{resume_text}

Score each category from 0 to 100:

- overall_score
- structure_score
- skills_score
- projects_score
- impact_score
- completeness_score

Also provide:
- strengths
- weaknesses
- recommendations

Be objective and give actionable recommendations.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": ResumeQuality,
            },
        )
    except Exception as exc:
        raise RuntimeError(
            "Unable to evaluate the resume with the AI service."
        ) from exc

    if response.parsed is not None:
        return response.parsed

    if response.text:
        try:
            return ResumeQuality.model_validate_json(response.text)
        except Exception as exc:
            raise RuntimeError(
                "The AI service returned an invalid resume-quality response."
            ) from exc

    raise RuntimeError("The AI service returned an empty response.")
