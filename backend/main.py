from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
<<<<<<< HEAD
from data_loader import router as data_loader_router
=======
from pydantic import BaseModel
from data_loader import router as data_loader_router
from task_allocator import allocate_task  # Import the AI task allocation function
>>>>>>> 7cb9f15f9b7bd4b67d9231480a2eb3e2e8397291

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

<<<<<<< HEAD
if __name__ == "__main__":
=======
if __name__ == "_main_":
>>>>>>> 7cb9f15f9b7bd4b67d9231480a2eb3e2e8397291
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
