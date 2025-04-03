from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data_loader import router as data_loader_router

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

@app.get("/")
def home():
    return {"message": "AI Task Allocation API is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
