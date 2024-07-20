from sqlalchemy import select
from database import new_session, TasksTable
from schemas import TaskInput, Task


class TaskRepository:
    @classmethod
    async def add_one(cls, data: TaskInput) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TasksTable(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls) -> list[Task]:
        async with new_session() as session:
            query = select(TasksTable)
            result = await session.execute(query)
            task_models = result.scalars().all()
            return task_models
