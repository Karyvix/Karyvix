import pymupdf
import pytest

from app.services.resume_parser import extract_text_from_pdf


def test_extract_text_from_pdf(tmp_path):
    pdf_path = tmp_path / "sample_resume.pdf"

    document = pymupdf.open()
    page = document.new_page()
    page.insert_text((72, 72), "Rishab Singh\nPython\nFastAPI")
    document.save(pdf_path)
    document.close()

    text = extract_text_from_pdf(str(pdf_path))

    assert "Rishab Singh" in text
    assert "Python" in text
    assert "FastAPI" in text


def test_extract_text_from_empty_pdf(tmp_path):
    pdf_path = tmp_path / "empty.pdf"

    document = pymupdf.open()
    document.new_page()
    document.save(pdf_path)
    document.close()

    with pytest.raises(
        ValueError,
        match="No readable text found in PDF.",
    ):
        extract_text_from_pdf(str(pdf_path))
