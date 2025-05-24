from uuid import UUID, uuid4
from decimal import Decimal

from fastapi import APIRouter

from point.view import PointPair, PlacePreview, Cost, MenuItem, PlaceOut
from point.view import fake, Point

router = APIRouter(tags=["Place"])


@router.post("s")
async def get_places(diagonal: PointPair) -> list[PlacePreview]:
    places: list[PlacePreview] = []

    for _ in range(fake.random_int(1, 10)):
        latitude = Decimal(fake.random_int(
            min=int(diagonal.lower.latitude * 10 ** 4),
            max=int(diagonal.upper.latitude * 10 ** 4),
            step=1
        )) / Decimal(10 ** 4)
        longitude = Decimal(fake.random_int(
            min=int(diagonal.lower.longitude * 10 ** 4),
            max=int(diagonal.upper.longitude * 10 ** 4),
            step=1
        )) / Decimal(10 ** 4)

        places.append(PlacePreview(
            id=uuid4(),
            name=fake.name(),
            photo=fake.image_url(),
            establishment_id=uuid4(),
            rating=fake.random_int(1, 5),
            position=Point(
                latitude=latitude,
                longitude=longitude,
                address=fake.address(),
            ),
        ))

    return places


@router.post("/{place_id}")
async def get_place(place_id: UUID) -> PlaceOut:
    return PlaceOut(
        id=place_id,
        name=fake.name(),
        description=fake.text(),
        icon=fake.image_url(),
        photo=fake.image_url(),
        gallery=[fake.image_url()],
        establishment_id=uuid4(),
        rating=fake.random_int(1, 5),
        menu=[MenuItem(
            title=fake.word(),
            description=fake.paragraph(),
            photo=fake.image_url(),
            cost=Cost(
                value=fake.random_int(1, 100),
                currency=fake.currency_symbol()
            ),
        ) for _ in range(fake.random_int(1, 10))],
        position=Point(
            latitude=fake.latitude(),
            longitude=fake.longitude(),
            address=fake.address(),
        ),
    )
