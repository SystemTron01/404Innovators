import pandas as pd
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/load_csv/")
def load_csv(file_path: str):
    try:
        df = pd.read_csv(file_path)
        return {"message": "CSV loaded successfully", "data": df.to_dict(orient="records")}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
