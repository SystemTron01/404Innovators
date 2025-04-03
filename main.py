from fastapi import FastAPI
from pydantic import BaseModel
from task_allocator import allocate_task  # Import the AI function

app = FastAPI()

# Request model for task and user data
class TaskRequest(BaseModel):
    task_desc: str
    user_skills: str  # A simple string representation for this example

@app.post("/assign")
async def assign_task(request: TaskRequest):
    assigned_user = allocate_task(request.task_desc, request.user_skills)
    return {"assigned_user": assigned_user}

