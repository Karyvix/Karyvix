import os

from dotenv import load_dotenv
from google import genai

from app.models.ai_analysis import AIAnalysis

load_dotenv()


def analyze_resume(resume_text: str, job_description: str) -> AIAnalysis:
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not configured.")

    client = genai.Client(api_key=api_key)

    prompt = f"""
Analyze the following resume against the provided job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Evaluate the candidate objectively.

Return:
- match_score: overall resume-to-job match from 0 to 100
- matched_skills: skills present in both the resume and job requirements
- missing_skills: important job requirements missing from the resume
- strengths: strongest aspects of the candidate for this role
- weaknesses: areas where the candidate is weaker for this role
- recommendations: specific actions the candidate should take to improve their fit
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": AIAnalysis,
            },
        )
    except Exception as exc:
        raise RuntimeError(
            "Unable to analyze the resume with the AI service."
        ) from exc

    if response.parsed is not None:
        return response.parsed

    if response.text:
        try:
            return AIAnalysis.model_validate_json(response.text)
        except Exception as exc:
            raise RuntimeError(
                "The AI service returned an invalid analysis response."
            ) from exc

    raise RuntimeError("The AI service returned an empty response.")
