from fastapi import FastAPI #FastAPI, currently installed in venv, ignore error.
from app.routes.resume import router as resume_router #To upload Resume
from app.routes.matching import router as matching_router

app = FastAPI(
    title="HirePilot AI",
    description="AI-powered career assistant",
    version="0.1.0"
) #Creates the application with desc and title

app.include_router(resume_router)
app.include_router(matching_router)

@app.get("/") #creates a get endpoint at "/"
def home(): #function runs when someone visits /
    return {
        "message": "Welcome to HirePilot AI",
        "status": "running"
    } #Fast api auto converts python dicts to json 

#visit http://127.0.0.1:8000/