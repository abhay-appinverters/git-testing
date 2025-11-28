# app/api/routes_todo.py


from typing import List
from fastapi import APIRouter, HTTPException
from app.models.todo import Todo, TodoCreate
from app.custom_exception.index import TodoNotFound

router = APIRouter(tags=["todos"])

# in-memory "DB"
todos: List[Todo] = []
_next_id = 1


@router.get("/todos", response_model=List[Todo])
def list_todos():
    return todos


@router.post("/todos", response_model=Todo)
def create_todo(payload: TodoCreate):
    global _next_id
    new_todo = Todo(id=_next_id, **payload.dict())
    _next_id += 1
    todos.append(new_todo)
    return new_todo


@router.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    # raise HTTPException(status_code=404, detail="Todo not found")
    raise TodoNotFound(todo_id=todo_id)


@router.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, payload: TodoCreate):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            updated = Todo(id=todo_id, **payload.dict())
            todos[index] = updated
            return updated
    # raise HTTPException(status_code=404, detail="Todo not found")
    raise TodoNotFound(todo_id=todo_id)


@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            del todos[index]
            return {"deleted": True}
    # raise HTTPException(status_code=404, detail="Todo not found")
    raise TodoNotFound(todo_id=todo_id)
