from fastapi import FastAPI #FastAPI, currently installed in venv, ignore error.
from fastapi.middleware.cors import CORSMiddleware

from app.routes.resume import router as resume_router #To upload Resume
from app.routes.career_analysis import router as career_analysis_router

# from app.routes.matching import router as matching_router
# from app.routes.ai_analysis import router as ai_analysis_router

app = FastAPI(
    title="HirePilot AI",
    description="AI-powered career assistant",
    version="0.2.0"
) #Creates the application with desc and title

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resume_router)
app.include_router(career_analysis_router)
# app.include_router(matching_router)
# app.include_router(ai_analysis_router)

@app.get("/") #creates a get endpoint at "/"
def home(): #function runs when someone visits /
    return {
        "message": "Welcome to HirePilot AI",
        "status": "running"
    } #Fast api auto converts python dicts to json 

#visit http://127.0.0.1:8000/