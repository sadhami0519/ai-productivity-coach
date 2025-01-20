from sqlalchemy import Boolean, Column, Integer, String, DateTime
from .database import Base
from datetime import datetime

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    status = Column(String)  # "complete" or "in_progress"
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(String)  # We'll use this to identify different users

class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    task = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)

class PomodoroSession(Base):
    __tablename__ = "pomodoro_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    completed = Column(Boolean, default=False)