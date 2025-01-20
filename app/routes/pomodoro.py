from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from .. import models
from ..database import get_db

router = APIRouter()

@router.post("/pomodoro/start")
async def start_pomodoro(user_id: str, db: Session = Depends(get_db)):
    """Start a new Pomodoro session"""
    # Default Pomodoro session is 25 minutes
    session = models.PomodoroSession(
        user_id=user_id,
        start_time=datetime.utcnow(),
        end_time=datetime.utcnow(),  # Will be updated when session ends
        completed=False
    )
    db.add(session)
    db.commit()
    db.refresh(session)
    return {
        "message": "Pomodoro session started",
        "session_id": session.id
    }

@router.post("/pomodoro/{session_id}/complete")
async def complete_pomodoro(session_id: int, db: Session = Depends(get_db)):
    """Mark a Pomodoro session as complete"""
    session = db.query(models.PomodoroSession).filter(
        models.PomodoroSession.id == session_id
    ).first()
    
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    
    session.completed = True
    session.end_time = datetime.utcnow()
    db.commit()
    return {"message": "Pomodoro session completed"}

@router.get("/pomodoro/{user_id}/stats")
async def get_pomodoro_stats(user_id: str, db: Session = Depends(get_db)):
    """Get user's Pomodoro statistics"""
    completed_sessions = db.query(models.PomodoroSession).filter(
        models.PomodoroSession.user_id == user_id,
        models.PomodoroSession.completed == True
    ).count()
    
    return {
        "total_completed_sessions": completed_sessions,
        "total_study_time": completed_sessions * 25  # in minutes
    }