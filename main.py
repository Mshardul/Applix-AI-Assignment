""" Main file for running the Project """

# External Libraries
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Internal Project Routers 
from routes.upload import router as upload_router
from routes.dummy_data import router as dummy_data_router
from routes.retrieve import router as retrieve_router

app = FastAPI(
    title="Applix AI Assignment - Temperature Monitoring App",
    description="API for uploading, retrieving, and analyzing temperature data.",
    version="1.0.0",
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc",  # Alternative API docs (Redoc)
    openapi_url="/openapi.json"  # OpenAPI schema
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Register routers
app.include_router(upload_router, prefix="/upload", tags=["Upload"])
app.include_router(dummy_data_router, prefix="/dummy_data", tags=["Dummy Data"])
app.include_router(retrieve_router, prefix="/retrieve", tags=["Retrieve"])
