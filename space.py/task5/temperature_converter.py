#!/usr/bin/python3

""" An API that converts temperatures between Celsius and Fahrenheit using query parameters.
Example: /convert_temp?temp=100&unit=celsius → 212"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/convert_temp")
def convert_temp(temp: float, unit: str):
    if unit.lower() == "celsius":
        return {"fahrenheit": temp * 9/5 + 32}
    elif unit.lower() == "fahrenheit":
        return {"celsius": (temp - 32) * 5/9}
    else:
        return {"error": "Invalid unit. Use 'celsius' or 'fahrenheit'"}
