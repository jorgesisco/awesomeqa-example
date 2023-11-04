"""Main module for FastAPI application."""""
import uvicorn
from fastapi import FastAPI
from app.routes import router

# Initialize FastAPI application
app = FastAPI()

# Register router with views
app.include_router(router)


if __name__ == "__main__":
    # Run application with uvicorn in development
    uvicorn.run("app.main:app", host="0.0.0.0", port=5001, reload=True)
