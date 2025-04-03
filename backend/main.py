from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data_loader import load_tasks, load_users

app = FastAPI()

# Enable CORS for frontend-backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change this for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AI Task Allocation API is running!"}

@app.get("/tasks")
def get_tasks():
    """Fetch all tasks from the CSV."""
    tasks = load_tasks("tasks.csv")
    return {"tasks": tasks}

@app.get("/users")
def get_users():
    """Fetch all users from the CSV."""
    users = load_users("users.csv")
    return {"users": users}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
