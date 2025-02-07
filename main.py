from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.upload import router as upload_router
from routes.dummy_data import router as dummy_data_router
from routes.retrieve import router as retrieve_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow React frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Register routers
app.include_router(upload_router, prefix="/upload", tags=["Upload"])
app.include_router(dummy_data_router, prefix="/dummy_data", tags=["API"])
app.include_router(retrieve_router, prefix="/retrieve", tags=["API"])

