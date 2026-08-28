from fastapi import APIRouter, UploadFile, File, HTTPException
import tempfile
import os

from app.services.resume_parser import extract_text_from_pdf


router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )

    file_content = await file.read()

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        temp_file.write(file_content)
        temp_file_path = temp_file.name

    try:
        text = extract_text_from_pdf(temp_file_path)

        return {
            "filename": file.filename,
            "text": text
        }

    finally:
        os.remove(temp_file_path)