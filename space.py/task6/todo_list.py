#!/usr/bin/python3

""" This is an API that manages a simple to-do list. It uses dependencies to handle the storage and retrieval of tasks. """

from fastapi import FastAPI, Depends

app = FastAPI()

tasks = []

def create_task(task: str):
    tasks.append(task)
    return {"task": task}

@app.post("/tasks")                          def add_task(Task=Depends(create_task)):
    return Task               

@app.get("/tasks")
def get_task():
    return tasks
