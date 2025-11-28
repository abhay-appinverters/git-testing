# app/main.py

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

import time

from .api.routes_example import router as example_router
from .api.routes_todo import router as todo_router
from .api.routes_todo_v2 import router as todo_router_v2
from .core.config import settings

from .errors.index import TodoNotFound

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)


# include router from another file
app.include_router(example_router, prefix=settings.api_prefix)
app.include_router(todo_router, prefix=settings.api_prefix)
app.include_router(todo_router_v2, prefix=settings.api_v2_prefix)


@app.middleware("http")
async def add_timing_header(request: Request, call_next):
    start = time.perf_counter()

    # request jaane se pehle yaha aaega
    response = await call_next(request)

    duration = (time.perf_counter() - start) * 1000  # ms
    response.headers["X-Process-Time-ms"] = f"{duration:.2f}"
    response.headers["X-App-Env"] = settings.env

    return response


@app.get("/")
def root():
    return {
        "message": "Hello from FastAPI + uv!",
        "env": settings.env,
    }


@app.exception_handler(TodoNotFound)
def todo_not_found_handler(request, exc: TodoNotFound):
    return JSONResponse(
        status_code=408, content={"error": f"Todo with ID {exc.todo_id} not found"}
    )
