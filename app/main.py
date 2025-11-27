# app/main.py

from fastapi import FastAPI
from .api.routes_example import router as example_router

app = FastAPI(title="My First FastAPI App")

# include router from another file
app.include_router(example_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Hello from FastAPI + uv!"}
