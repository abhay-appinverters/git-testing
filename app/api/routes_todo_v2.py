# app/api/routes_todo_v2.py


from typing import List

from fastapi import APIRouter, HTTPException, Response, status

from app.models.todo import Todo, TodoCreate

router = APIRouter(tags=["todos_v2"])

todos: List[Todo] = []
_next_id = 1


def setResponseHeaders(
    response: Response, status_code: int, apiEndpoint: str | None = None
):
    response.status_code = status_code
    if apiEndpoint:
        response.headers["Location"] = apiEndpoint
    return response


@router.post("/todos", response_model=Todo)
def create_todo(payload: TodoCreate, response: Response):
    global _next_id
    new_todo = Todo(id=_next_id, **payload.dict())
    _next_id += 1
    todos.append(new_todo)

    response = setResponseHeaders(
        response, status.HTTP_201_CREATED, f"/api_v2/todos/{new_todo.id}"
    )
    return new_todo


# get all todos
@router.get("/todos", response_model=List[Todo])
def list_todos():
    return todos


# search : get todo by title
@router.get("/todos/search", response_model=List[Todo])
def search_todo(limit: int = 10, q: str | None = None):
    results = []
    for todo in todos:
        if q and q.lower() in todo.title.lower():
            results.append(todo)
        if len(results) >= limit:
            break
    if results:
        print("Search results:", results)
        return results
    raise HTTPException(status_code=404, detail="Todo not found")


# delete with 204 No Content by todo id
@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, response: Response):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            del todos[index]
            response = setResponseHeaders(response, status.HTTP_204_NO_CONTENT)
            return response
    raise HTTPException(status_code=404, detail="Todo not found")
