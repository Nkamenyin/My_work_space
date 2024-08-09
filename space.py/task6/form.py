#!/usr/bin/python3

""" This is an API to handle contact form submissions. Use form data to receive input from users and error handling to validate required fields, returning appropriate status codes for missing or invalid data"""
 
from fastapi import FastAPI, Form, HTTPException, Annotated
from pydantic import BaseModel

app = FastAPI()

class ContactForm(BaseModel):
    name: str
    email: str

@app.post("/contact")
def contact_form(name: Annotated[str, Form()], email: Annotated[str, Form()]):
    if not name or not email or not message:
        raise HTTPException(status_code=400, detail="All fields are required")
    return {"message": "Submission successful"}
