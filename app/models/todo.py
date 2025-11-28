# app/models/todo.py


from pydantic import BaseModel, Field, field_validator


class TodoBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=50)
    completed: bool = False

    @field_validator("title")
    def no_hack_and_empty(cls, v):
        if "hack" in v.lower():
            raise ValueError("Title cannot contain the word 'hack'")
        if not v.strip():
            raise ValueError("Title cannot be empty or whitespace")
        return v


class TodoCreate(TodoBase):
    """Data required when creating a todo"""

    pass


class Todo(TodoBase):
    id: int

    class Config:
        from_attributes = True
