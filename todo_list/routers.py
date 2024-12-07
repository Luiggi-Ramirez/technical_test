from fastapi import APIRouter, Response, HTTPException
from todo_list.schemas import TodoBaseModel

router = APIRouter()

tasks = [
    {"id": 1, "title": "tarea 1", "description": "tarea 1", "completed": False},
    {"id": 2, "title": "tarea 2", "description": "tarea 2", "completed": False},
    {"id": 3, "title": "tarea 3", "description": "tarea 3", "completed": False},
]


@router.post("/tasks/")
async def create_task(r: Response, todo: TodoBaseModel):
    # se obtienen una lista con ids
    tasks_ids = [task["id"] for task in tasks]
    # se valida si el id que se ingresa no existe en la lista
    if todo.id not in tasks_ids:
        # se guarda la data en la lista
        tasks.append(dict(todo))
        # se selecciona el codigo http
        r.status_code = 201
        # se retorna la data guardada
        return todo
    # en el caso de que el id ya este guardado se retorna un error
    raise HTTPException(status_code=400, detail=f"task with id {todo.id} exists")


@router.get("/tasks/")
async def get_tasks():
    if not tasks:
        raise HTTPException(status_code=404, detail="tasks not found")
    return tasks


@router.get("/tasks/{id}/")
async def get_task(id: int):
    for task in tasks:
        if id == task["id"]:
            return task
    raise HTTPException(status_code=404, detail="task not found")


@router.put("/tasks/{id}/")
async def update_task(id: int, todo: TodoBaseModel):
    for task in tasks:
        if id == task["id"]:
            task["title"] = todo.title
            task["description"] = todo.description
            task["completed"] = todo.completed
            return task
    raise HTTPException(status_code=404, detail="task not found")


@router.delete("/tasks/{id}/")
async def delete_task(r: Response, id: int):
    for task in tasks:
        if id == task["id"]:
            tasks.remove(task)
            r.status_code = 204
            return
    raise HTTPException(status_code=404, detail="task not found")
