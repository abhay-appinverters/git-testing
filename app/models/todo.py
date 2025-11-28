# app/models/todo.py

from pydantic import BaseModel
from typing import Optional

class TodoBase(BaseModel):
    title: str
    completed: bool = False

class TodoCreate(TodoBase):
    """Data required when creating a todo"""
    pass

class Todo(TodoBase):
    id: int

    class Config:
        from_attributes = True
