from app.db.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, ForeignKey, Enum
from datetime import datetime, timezone
import enum

# Enum for task status
class TaskStatus(str, enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"


# Model Task
class Task(Base):
    __tablename__ = "task"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True, nullable=False)
    description = Column(Text, nullable=False)
    status = Column(Enum(TaskStatus, name="task_status"), default=TaskStatus.pending, index=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(tz=timezone.utc), nullable=False)
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(tz=timezone.utc), onupdate=lambda: datetime.now(tz=timezone.utc), nullable=False)
    created_by = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False)
    