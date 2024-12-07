import strawberry
from typing import Optional


# definimos la clase para el mapeo de schemas
@strawberry.type
class Task:
    id: int
    title: str
    description: Optional[str] = None
    completed: bool


# se definen los datos de entrada para crear tareas
@strawberry.input
class TaskInput:
    id: int
    title: str
    description: Optional[str] = None
    completed: bool


# se definen los datos de entrada para actualizar tareas
@strawberry.input
class UpdateTaskInput:
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
