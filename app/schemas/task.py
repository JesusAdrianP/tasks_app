from pydantic import BaseModel
from app.models.task import TaskStatus
from typing import Optional
from datetime import datetime

#Validation base schema for task
class TaskBase(BaseModel):
    title: str
    description: str
    status: TaskStatus = TaskStatus.pending
    
#validation for creating a task
class TaskCreate(TaskBase):
    pass

#validation for updating a task
class TaskUpdate(BaseModel):
    title: Optional[str]=None
    description: Optional[str]=None
    status: Optional[TaskStatus] = None
    

#validation for user output
class TaskOut(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    
    model_config = {
        "from_attributes": True
    }

#validation for paginated task output
class PaginatedTasks(BaseModel):
    total: int
    page: int
    page_size: int
    data: list[TaskOut]
