import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from app.models.resume_quality import ResumeQuality


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment.")

client = genai.Client(api_key=api_key)


def analyze_resume_quality(resume_text: str) -> ResumeQuality:

    prompt = f"""
You are an expert technical recruiter and professional resume reviewer.

Evaluate the following resume independently of any particular job.

Do not invent information that is not present in the resume.

Evaluate:

1. Structure and readability
2. Technical skills clarity and relevance
3. Quality and relevance of projects
4. Measurable achievements and demonstrated impact
5. Overall completeness

Give practical and honest feedback.

RESUME:
{resume_text}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=ResumeQuality,
        ),
    )

    if response.parsed:
        return response.parsed

    return ResumeQuality.model_validate_json(response.text)