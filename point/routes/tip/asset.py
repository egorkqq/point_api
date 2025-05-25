from decimal import Decimal
from uuid import uuid4

from fastapi import APIRouter, Depends

from point.auth import get_user
from point.view import AuthUser, AssetOut, fake, random_address

router = APIRouter(tags=["Asset"])


@router.get("s")
async def get_assets(_: AuthUser = Depends(get_user)) -> list[AssetOut]:
    return [AssetOut(
        id=uuid4(),
        name=fake.cryptocurrency_name(),
        ticker=fake.currency_symbol(),
        price=Decimal(fake.random_int(1, 1000)) / Decimal(500),
        address=random_address(),
        icon=fake.image_url(1280, 720),
    ) for _ in range(fake.random_int(1, 10))]
