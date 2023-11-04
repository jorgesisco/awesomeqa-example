"""Main module for FastAPI application."""""
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router

# Initialize FastAPI application
app = FastAPI()

# Register CORS middleware to allow specific origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],  # The methods you want to allow
    allow_headers=["*"],  # The headers you want to allow
)

# Register router with views
app.include_router(router)


if __name__ == "__main__":
    # Run application with uvicorn in development
    uvicorn.run("app.main:app", host="0.0.0.0", port=5001, reload=True)
