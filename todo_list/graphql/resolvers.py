from typing import List, Optional
from todo_list.graphql.schemas import Task, TaskInput, UpdateTaskInput

# lista que simula db
tasks = [
    {"id": 1, "title": "tarea 1", "description": "tarea 1", "completed": False},
    {"id": 2, "title": "tarea 2", "description": "tarea 2", "completed": False},
    {"id": 3, "title": "tarea 3", "description": "tarea 3", "completed": False},
]


def create_task(input: TaskInput) -> Task:
    new_task = {
        "id": input.id,
        "title": input.title,
        "description": input.description,
        "completed": input.completed,
    }
    # se obtienen una lista con ids
    tasks_ids = [task["id"] for task in tasks]
    # se valida si el id que se ingresa no existe en la lista
    if new_task["id"] not in tasks_ids:
        # se guarda la data en la lista
        tasks.append(new_task)
        return Task(**new_task)
    raise Exception("Task exist")


# resolver para obtener todas las tareas
def get_tasks() -> List[Task]:
    return [Task(**task) for task in tasks]


# resolver para obtener una tarea
def get_task_by_id(id: int) -> Optional[Task]:
    try:
        task = [task for task in tasks if task["id"] == id][0]
        return Task(**task)
    except Exception:
        raise Exception("Task does not exist")


# resolver para actualizar tarea
def update_task(id: int, input: UpdateTaskInput) -> Task:
    try:
        task = [task for task in tasks if task["id"] == id][0]
    except Exception:
        raise Exception("Task does not exist")
    # Actualizar los campos modificados
    if input.title is not None:
        task["title"] = input.title
    if input.description is not None:
        task["description"] = input.description
    if input.completed is not None:
        task["completed"] = input.completed
    return Task(**task)


# resolver para eliminar tarea
def delete_task(id: int) -> str:
    try:
        task = [task for task in tasks if task["id"] == id][0]
        tasks.remove(task)
        return "Task deleted"
    except Exception:
        raise Exception("Task does not exist")
