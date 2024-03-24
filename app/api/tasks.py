from fastapi import APIRouter, HTTPException
from typing import List
from models.tasks import Task
from db.fake_db import tasks_db

router = APIRouter()


@router.post("/tasks/")
def create_task(task: Task):
    tasks_db.append(task)
    return task


@router.get("/tasks/")
def read_tasks():
    print(tasks_db)
    return tasks_db


@router.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    if task_id >= len(tasks_db):
        raise HTTPException(status_code=404, detail="Task not found")
    tasks_db[task_id] = task
    return task


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id >= len(tasks_db):
        raise HTTPException(status_code=404, detail="Task not found")
    deleted_task = tasks_db.pop(task_id)
    return deleted_task
