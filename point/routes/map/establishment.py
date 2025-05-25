from uuid import UUID, uuid4

from fastapi import APIRouter

from point.view import EstablishmentOut, fake

router = APIRouter(tags=["Establishment"])


@router.post("s")
async def get_establishments() -> dict[UUID, EstablishmentOut]:
    establishments: dict[UUID, EstablishmentOut] = {}

    for _ in range(fake.random_int(1, 10)):
        establishments[uuid4()] = EstablishmentOut(
            id=uuid4(),
            name=fake.name(),
            icon=fake.image_url(1280, 720),
        )

    return establishments
