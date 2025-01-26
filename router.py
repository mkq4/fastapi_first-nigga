from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STaskAdd, STask, SAddTask

router = APIRouter(prefix='/tasks', tags=['tasks'])

@router.post("")
async def addTask(task: Annotated[STaskAdd, Depends()]) -> SAddTask:
    task_id: int = await TaskRepository.add_one(task)
    return {'ok': True, "task_id": task_id}

@router.get("")
async def getTasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks