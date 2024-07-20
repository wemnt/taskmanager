from pydantic import BaseModel


class TaskInput(BaseModel):
    name: str
    description: str | None


class Task(TaskInput):
    id: int
