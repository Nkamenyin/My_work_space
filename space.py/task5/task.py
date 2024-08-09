#!/usr/bin/python3

"""Develop an API to manage a simple to-do list with endpoints to add, view, and delete tasks.
Use request body to add tasks and path parameters to identify tasks.
Example: POST /tasks with request body {"task":"Buy groceries"}"""

from fastapi import FastAPI, HTTPException

app = FastAPI()

tasks = [] #creating a list to store tasks

@app.post("/tasks")
def create_task(task: str):
    tasks.append(task)
    return {"task": task}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    try:
        del tasks[task_id]
        return {"message": "Task deleted"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Task not found")
