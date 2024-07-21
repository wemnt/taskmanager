from typing import Annotated
from fastapi import APIRouter, Depends
from repository import TaskRepository
from schemas import TaskInput, Task, TaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks:"],
)

tasks = []


@router.post("")
async def create_task(
        task: Annotated[TaskInput, Depends()]
) -> TaskId:
    new_task_id = await TaskRepository.add_one(task)
    return {"id": new_task_id}
@router.get("")
async def get_task() -> list[Task]:
    tasks = await TaskRepository.find_all()
    return tasks