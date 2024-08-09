#!/usr/bin/python3

""" Create an API that takes a string as a query parameter and returns its length. Example: /length?text=hello → 5 """

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/length")
def string_length(text: str = Query()):
    return {"length": len(text)}
