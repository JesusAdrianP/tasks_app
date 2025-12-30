from fastapi import APIRouter, status, Depends, Query, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.schemas.task import TaskCreate, TaskOut, TaskUpdate, PaginatedTasks
from app.services.task_service import create_task, get_task_by_id, get_paginated_tasks, update_task, delete_task
from app.db.dependencies import get_db
from app.core.dependencies import get_current_user

router = APIRouter()

#endpoint to create a new task
@router.post("/create_task", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_new_task(payload: TaskCreate, db:Session = Depends(get_db), current_user = Depends(get_current_user)):
    return create_task(db, task_in=payload, user_id=current_user.id)

#endpoint to get tasks created by the current user
@router.get("/my_taks", response_model=PaginatedTasks, status_code=status.HTTP_200_OK)
def list_user_tasks(db:Session = Depends(get_db), current_user = Depends(get_current_user), page: int = Query(1, ge=1), page_size: int = Query(10, ge=1, le=100)):
    total, tasks =  get_paginated_tasks(db, current_user.id, page, page_size)
    return PaginatedTasks(total=total, page=page, page_size=page_size, data=tasks)

#endpoint to get a task by id
@router.get("/{task_id}", response_model=TaskOut, status_code=status.HTTP_200_OK)
def get_task(task_id:int, db:Session = Depends(get_db), current_user = Depends(get_current_user)):
    return get_task_by_id(db, task_id, current_user.id)

#endpoint to update a task
@router.put("/update/{task_id}", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def update_task_by_id(task_id:int, payload:TaskUpdate, db:Session = Depends(get_db), current_user = Depends(get_current_user)):
    task = get_task_by_id(db, task_id, current_user.id)
    if not task:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message":"Task not found"})
    
    return update_task(db, task, payload)

#endpoint to delete a task
@router.delete("/delete/{task_id}", status_code=status.HTTP_200_OK)
def delete_task_by_id(task_id:int, db:Session = Depends(get_db), current_user = Depends(get_current_user)):
    task = get_task_by_id(db, task_id, current_user.id)
    if not task:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message":"Task not found"})
    
    delete_task(db, task)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Task deleted successfully"})