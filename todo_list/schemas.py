from pydantic import BaseModel


# Base Model API
class TodoBaseModel(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
