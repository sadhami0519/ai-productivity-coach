# routes/schedule.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List
from .. import models
from ..database import get_db

router = APIRouter()

@router.post("/schedule/")
async def create_schedule(
    task: str,
    start_time: datetime,
    end_time: datetime,
    user_id: str,
    db: Session = Depends(get_db)
):
    """Create a new schedule entry for a study session"""
    schedule = models.Schedule(
        user_id=user_id,
        task=task,
        start_time=start_time,
        end_time=end_time
    )
    db.add(schedule)
    db.commit()
    db.refresh(schedule)
    return schedule

@router.get("/schedule/{user_id}")
async def get_schedule(user_id: str, db: Session = Depends(get_db)):
    """Get all scheduled tasks for a user"""
    schedules = db.query(models.Schedule).filter(
        models.Schedule.user_id == user_id
    ).all()
    return schedules

@router.delete("/schedule/{schedule_id}")
async def delete_schedule(schedule_id: int, db: Session = Depends(get_db)):
    """Delete a scheduled task"""
    schedule = db.query(models.Schedule).filter(
        models.Schedule.id == schedule_id
    ).first()
    if not schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")
    db.delete(schedule)
    db.commit()
    return {"message": "Schedule deleted successfully"}