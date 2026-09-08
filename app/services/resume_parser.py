import pymupdf


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extracts text from a PDF resume.

    Args:
        file_path: Path to the PDF file.

    Returns:
        Extracted text from all pages.
    """
    document = pymupdf.open(file_path)

    try:
        text = ""

        for page in document:
            text += page.get_text()

        text = text.strip()

        if not text:
            raise ValueError("No readable text found in PDF.")

        return text

    finally:
        document.close()