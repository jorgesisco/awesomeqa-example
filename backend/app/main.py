"""Main module for FastAPI application."""""
# pylint: disable=import-error
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from app.routes import router
from app.utils.rate_limit import limiter


def create_app() -> FastAPI:
    # Initialize FastAPI application
    app = FastAPI()

    # Register the rate limit exceeded handler
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

    # Register CORS middleware to allow specific origins
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],  # The methods you want to allow
        allow_headers=["*"],  # The headers you want to allow
    )

    # Register router with views
    app.include_router(router)

    return app


app = create_app()

if __name__ == "__main__":
    # Run application with uvicorn in development
    uvicorn.run("app.main:app", host="0.0.0.0", port=5001, reload=True)
