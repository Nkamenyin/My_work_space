#!/usr/bin/python3

""" An API that accepts multi-part form data, such as a form with both text and file inputs (e.g., a job application form with resume uploads). Use dependencies to validate inputs and error handling for missing or invalid data"""

from fastapi import FastAPI, File, UploadFile, Form, Depends, HTTPException, Annotated

app = FastAPI()

 def validate_job_application(name: Annotated[str, Form()], email: Annotated[str, Form()], resume: UploadFile = File()):
    if not name or not email:
        raise HTTPException(status_code=400, detail="Name and email are required")
    if not resume:
        raise HTTPException(status_code=400, detail="Resume is required")
    return {"name": name, "email": email, "resume": resume}

@app.post("/application")
def job_application_handler(job_application=Depends(validate_job_application)):
    return {"message": "Application submitted sucessfully"}
