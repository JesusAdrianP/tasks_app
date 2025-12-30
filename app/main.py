from fastapi import FastAPI
from app.api.v1 import users, auth, task

app = FastAPI()
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(task.router, prefix="/api/task", tags=["Tasks"])

@app.get("/")
def read_root():
    return {"message": "Hello world"}