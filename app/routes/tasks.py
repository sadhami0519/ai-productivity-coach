from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from .. import models, schemas
from ..database import get_db

router = APIRouter()

@router.post("/tasks/", response_model=schemas.Task)
async def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    """
    Create a new task for a student.
    This function takes the task details and saves them to the database.
    """
    db_task = models.Task(
        title=task.title,
        description=task.description,
        status="in_progress",  # New tasks start as in_progress
        user_id=task.user_id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.get("/tasks/{user_id}", response_model=List[schemas.Task])
async def get_user_tasks(user_id: str, db: Session = Depends(get_db)):
    """
    Retrieve all tasks for a specific user.
    This helps students keep track of their ongoing and completed tasks.
    """
    tasks = db.query(models.Task).filter(models.Task.user_id == user_id).all()
    return tasks

@router.put("/tasks/{task_id}", response_model=schemas.Task)
async def update_task_status(
    task_id: int, 
    status: str, 
    db: Session = Depends(get_db)
):
    """
    Update the status of a task (complete/in_progress).
    This allows students to mark tasks as done or return them to in-progress.
    """
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    if status not in ["complete", "in_progress"]:
        raise HTTPException(status_code=400, detail="Invalid status")
    
    task.status = status
    db.commit()
    db.refresh(task)
    return task

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    """
    Delete a task from the system.
    This lets students remove tasks they no longer need to track.
    """
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}