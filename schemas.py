from typing import Optional
from pydantic import BaseModel


class TaskInput(BaseModel):
    name: str
    description: Optional[str]


class Task(TaskInput):
    id: int


class TaskId(BaseModel):
    ok: bool = True
    task_id: int
