from fastapi import FastAPI
from backend.data_loader import router as data_loader_router
from pydantic import BaseModel
from task_allocator import allocate_task

app = FastAPI()

# Register the data_loader router
app.include_router(data_loader_router)

# Request model for task and user data
class TaskRequest(BaseModel):
    task_desc: str
    user_skills: str

@app.post("/assign")
async def assign_task(request: TaskRequest):
    assigned_user = allocate_task(request.task_desc, request.user_skills)
    return {"assigned_user": assigned_user}

@app.get("/")
def home():
    return {"message": "AI Task Allocation API is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
