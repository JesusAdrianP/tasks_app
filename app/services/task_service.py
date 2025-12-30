from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate
from fastapi import HTTPException, status

#service for creating a new task
def create_task(db:Session, task_in:TaskCreate, user_id: int):
    task = Task(
        title=task_in.title,
        description=task_in.description,
        status=task_in.status,
        created_by=user_id
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

#service for getting a tasks created by a user
def get_paginated_tasks(db:Session, user_id:int, page: int = 1, page_size: int = 10):
    total = db.query(Task).filter(Task.created_by == user_id).count()
    offset = (page - 1) * page_size
    tasks = db.query(Task).filter(Task.created_by==user_id).offset(offset).limit(page_size).all()
    return total, tasks

#service for getting a task by id
def get_task_by_id(db:Session, task_id:int, user_id:int):
    task = db.query(Task).filter(Task.id==task_id, Task.created_by==user_id).first()
    
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    
    return task

#service for updating a task
def update_task(db:Session, task:Task, task_data:TaskUpdate):
    update_data = task_data.model_dump(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(task,field,value)
    
    db.commit()
    db.refresh(task)
    return task
    
#service for deleting a task
def delete_task(db:Session, task):
    db.delete(task)
    db.commit()