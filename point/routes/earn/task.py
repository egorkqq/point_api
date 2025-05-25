from uuid import uuid4

from fastapi import APIRouter, Depends

from point.auth import get_user
from point.view import AuthUser, TaskOut, fake

router = APIRouter()


@router.get("s")
async def get_tasks(user: AuthUser = Depends(get_user)) -> list[TaskOut]:
    tasks = [TaskOut(
        id=uuid4(),
        title=fake.name(),
        description=fake.text(),
        profit=fake.random_int(1, 10 ** 10),
        done=fake.boolean(),
    ) for _ in range(fake.random_int(1, 10))]

    tasks.sort(key=lambda task: task.done, reverse=True)
    return tasks
