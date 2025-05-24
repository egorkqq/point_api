from uuid import uuid4

from fastapi import APIRouter, Depends

from point.auth import get_user
from point.view import AuthUser, TaskOut, fake

router = APIRouter()


@router.get("s")
async def get_tasks(user: AuthUser = Depends(get_user)) -> list[TaskOut]:
    return [TaskOut(
        id=uuid4(),
        title=fake.name(),
        description=fake.text(),
        profit=fake.random_int(1, 10 ** 10),
    ) for _ in range(fake.random_int(1, 10))]
