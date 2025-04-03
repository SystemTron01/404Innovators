from fastapi import FastAPI
from backend.data_loader import router as data_loader_router

app = FastAPI()

# Register the data_loader router
app.include_router(data_loader_router)
