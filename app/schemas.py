from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class TaskBase(BaseModel):
    """
    Base class for Task data - contains fields common to all task operations
    """
    title: str
    description: Optional[str] = None
    user_id: str

class TaskCreate(TaskBase):
    """
    Schema for creating a new task - inherits from TaskBase
    We might add more fields specific to task creation here
    """
    pass

class Task(TaskBase):
    """
    Schema for returning task data - includes all task fields
    This represents how tasks look when sent back to the user
    """
    id: int
    status: str
    created_at: datetime

    class Config:
        """Tell Pydantic to work with ORM models"""
        from_attributes = True

class ScheduleBase(BaseModel):
    """
    Base class for Schedule data
    """
    task: str
    user_id: str
    start_time: datetime
    end_time: datetime

class ScheduleCreate(ScheduleBase):
    """
    Schema for creating a new schedule entry
    """
    pass

class Schedule(ScheduleBase):
    """
    Complete schedule entry with all fields
    """
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class PomodoroSession(BaseModel):
    """
    Schema for Pomodoro session data
    """
    id: int
    user_id: str
    start_time: datetime
    end_time: Optional[datetime]
    completed: bool

    class Config:
        from_attributes = True