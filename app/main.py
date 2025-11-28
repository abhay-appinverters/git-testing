# app/main.py

from fastapi import FastAPI

from .api.routes_example import router as example_router
from .api.routes_todo import router as todo_router
from .api.routes_todo_v2 import router as todo_router_v2
from .core.config import settings

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)


# include router from another file
app.include_router(example_router, prefix=settings.api_prefix)
app.include_router(todo_router, prefix=settings.api_prefix)
app.include_router(todo_router_v2, prefix=settings.api_v2_prefix)


@app.get("/")
def root():
    return {
        "message": "Hello from FastAPI + uv!",
        "env": settings.env,
    }
