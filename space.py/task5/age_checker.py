#!/usr/bin/python3

""" This API that checks if a user is an adult based on their age provided as a path parameter. Example: /check_age/20 → "Adult" or "Not an adult" """

from fastapi import FastAPI

app = FastAPI()

@app.get("/check_age/{age}")
def check_age(age: int):
    if age >= 18:
        return {"status": "Adult"}
    else:
        return {"status": "Not an adult"}
