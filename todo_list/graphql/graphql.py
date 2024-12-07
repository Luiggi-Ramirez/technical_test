import strawberry
from typing import List
from todo_list.graphql.resolvers import (
    Task,
    get_tasks,
    get_task_by_id,
    create_task,
    update_task,
    delete_task,
)


# class query para consultas
@strawberry.type
class Query:
    # obtener todas las tareas
    tasks: List[Task] = strawberry.field(resolver=get_tasks)
    # obtener el detalle de una tarea
    task: Task = strawberry.field(resolver=get_task_by_id)


# class mutation para crear, actualizar y eliminar tareas
@strawberry.type
class Mutation:
    # crear nueva tarea
    createTask: Task = strawberry.field(resolver=create_task)
    # actualizar una tarea
    updateTask: Task = strawberry.field(resolver=update_task)
    # eliminar una tarea
    deleteTask: str = strawberry.field(resolver=delete_task)


# creamos el schema tomando las clases
schema = strawberry.Schema(query=Query, mutation=Mutation)
