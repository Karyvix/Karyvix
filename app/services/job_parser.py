def clean_job_description(text: str) -> str:
    """
    Clean and normalize a job description.

    Args:
        text: Raw job description.

    Returns:
        Cleaned job description.
    """

    text = text.strip()

    lines = text.splitlines()

    cleaned_lines = []

    for line in lines:
        line = line.strip()

        if line:
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines)