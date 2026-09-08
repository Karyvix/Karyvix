import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from app.models.ai_analysis import AIAnalysis


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment.")

client = genai.Client(api_key=api_key)


def analyze_resume(
    resume_text: str,
    job_description: str
) -> AIAnalysis:

    prompt = f"""
You are an expert technical recruiter and resume evaluator.

Analyze the candidate's resume against the provided job description.

Your analysis must be based only on the information present in the
resume and job description. Do not invent experience, skills, education,
or achievements.

Evaluate:
- Overall suitability for the role
- Skills demonstrated by the candidate
- Important skills required by the job that are missing or unclear
- Candidate strengths
- Candidate weaknesses
- Specific recommendations for improving the candidate's fit

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=AIAnalysis,
        ),
    )

    if response.parsed:
        return response.parsed

    return AIAnalysis.model_validate_json(response.text)