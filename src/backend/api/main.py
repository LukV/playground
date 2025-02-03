"""FastAPI application."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Root endpoint returning a welcome message."""
    return {"message": "Hello World"}
