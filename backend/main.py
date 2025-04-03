from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from data_loader import router as data_loader_router
from task_allocator import allocate_task  # Import the AI task allocation function

app = FastAPI()

# Register the data_loader router
app.include_router(data_loader_router)

# Enable CORS for frontend-backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Change to frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model for task and user data
class TaskRequest(BaseModel):
    task_desc: str
    user_skills: str  # A simple string representation for this example

# Task assignment endpoint
@app.post("/assign")
async def assign_task(request: TaskRequest):
    assigned_user = allocate_task(request.task_desc, request.user_skills)
    return {"assigned_user": assigned_user}

@app.get("/")
def home():
    return {"message": "AI Task Allocation API is running!"}

if _name_ == "_main_":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
