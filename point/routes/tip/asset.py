from fastapi import APIRouter, Depends

from point.auth import get_user
from point.view import AuthUser, AssetOut, fake, random_address

router = APIRouter(tags=["Asset"])


@router.get("s")
async def get_assets(_: AuthUser = Depends(get_user)) -> list[AssetOut]:
    return [AssetOut(
        name=fake.currency_name(),
        ticker=fake.currency_symbol(),
        address=random_address(),
        icon=fake.image_url(),
    ) for _ in range(fake.random_int(1, 10))]
