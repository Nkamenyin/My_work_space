#!/usr/bin/python3

""" An API that calculates BMI based on weight and height provided in the request body.
Example: POST /bmi with request body { "weight": 70, "height": 1.75 }"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model for BMI input
class Bmi_request(BaseModel):
    weight: float
    height: float

@app.post("/bmi")
def calculate_bmi(input: Bmi_request):
    bmi = input.weight / input.height ** 2
    return {"bmi": bmi}
