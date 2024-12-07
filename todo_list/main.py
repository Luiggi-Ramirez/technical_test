from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from todo_list.routers import router
from todo_list.graphql.graphql import schema

app = FastAPI(title="Todo List API")

graphql_app = GraphQLRouter(schema=schema)

app.include_router(router=router, tags=["Tareas"])
app.include_router(graphql_app, prefix="/graphql")
