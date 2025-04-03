import pandas as pd
from fastapi import APIRouter, HTTPException

router = APIRouter()

# Define allowed files
CSV_FILES = {
    "tasks": "backend/data/tasks.csv",
    "users": "backend/data/users.csv"
}

@router.get("/load_csv/")
def load_csv(file_type: str):
    """Loads predefined CSV files (tasks or users) based on query parameter."""
    if file_type not in CSV_FILES:
        raise HTTPException(status_code=400, detail="Invalid file type. Use 'tasks' or 'users'.")

    file_path = CSV_FILES[file_type]
    
    try:
        df = pd.read_csv(file_path)
        return {"message": f"{file_type.capitalize()} CSV loaded successfully", "data": df.to_dict(orient="records")}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error loading CSV: {str(e)}")
