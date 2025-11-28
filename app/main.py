# app/main.py

from fastapi import FastAPI
from .api.routes_example import router as example_router
from .api.routes_todo import router as todo_router

from .core.config import APP_NAME

app = FastAPI(title=APP_NAME)


# include router from another file
app.include_router(example_router, prefix="/api")
app.include_router(todo_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Hello from FastAPI + uv!"}
