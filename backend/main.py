from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data_loader import load_tasks, load_users

app = FastAPI()

# Enable CORS for frontend-backend communication (Change "http://localhost:3000" to your actual frontend URL if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Change to frontend URL
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
    try:
        tasks = load_tasks("tasks.csv")
        return {"tasks": tasks}
    except Exception as e:
        return {"error": f"Failed to load tasks: {str(e)}"}

@app.get("/users")
def get_users():
    """Fetch all users from the CSV."""
    try:
        users = load_users("users.csv")
        return {"users": users}
    except Exception as e:
        return {"error": f"Failed to load users: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
