from typing import Annotated
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from repository import TaskRepository
from schemas import TaskInput

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks:"],
)

tasks = []


class TaskId(BaseModel):
    id: int


@router.post("")
async def create_task(
        task: Annotated[TaskInput, Depends()]
) -> TaskId:
    new_task_id = await TaskRepository.add_one(task)
    return {"id": new_task_id}
@router.get("")
async def get_task():
    tasks = await TaskRepository.find_all()
    return {"data": tasks}