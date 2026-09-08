from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form,
    HTTPException
)

from app.services.resume_parser import extract_text_from_pdf
from app.services.ai_analyzer import analyze_resume


router = APIRouter(
    prefix="/ai",
    tags=["AI Analysis"]
)


@router.post("/analyze")
async def analyze_uploaded_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )

    if not job_description.strip():
        raise HTTPException(
            status_code=400,
            detail="Job description cannot be empty."
        )

    file_content = await file.read()

    if not file_content:
        raise HTTPException(
            status_code=400,
            detail="Uploaded file is empty."
        )

    import tempfile
    import os

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        temp_file.write(file_content)
        temp_file_path = temp_file.name

    try:

        try:
            resume_text = extract_text_from_pdf(
                temp_file_path
            )

        except ValueError as error:
            raise HTTPException(
                status_code=400,
                detail=str(error)
            )

        result = analyze_resume(
            resume_text,
            job_description
        )

        return {
            "filename": file.filename,
            "analysis": result
        }

    finally:
        os.remove(temp_file_path)