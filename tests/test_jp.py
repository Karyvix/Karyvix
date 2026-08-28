from app.services.job_parser import clean_job_description


job_description = """

    Python Developer


    Required Skills:

    Python
    FastAPI
    SQL
    REST APIs


    Good communication skills.

"""


cleaned_text = clean_job_description(job_description)

print(cleaned_text)