from uuid import UUID, uuid4

from fastapi import APIRouter, Depends

from point.auth import get_user
from point.view import AuthUser, EmployeeReceiver, ReceiversOut, fake, random_address

router = APIRouter()


@router.get("s/{place_id}")
async def get_receivers(place_id: UUID, _: AuthUser = Depends(get_user)) -> ReceiversOut:
    return ReceiversOut(
        place_wallet=fake.random_element([None, random_address()]),
        employees=[EmployeeReceiver(
            id=uuid4(),
            name=fake.name(),
            profession="waiter",
            icon=fake.image_url(1280, 720),
        ) for _ in range(fake.random_int(1, 10))],
    )
