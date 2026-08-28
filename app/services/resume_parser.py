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

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text