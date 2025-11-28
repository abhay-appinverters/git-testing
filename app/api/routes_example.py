# app/api/routes_example.py

from fastapi import APIRouter

router = APIRouter(tags=["example"])

@router.get("/ping")
def ping():
    return {"status": "ok", "message": "pong"}
