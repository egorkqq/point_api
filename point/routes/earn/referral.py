from math import ceil

from fastapi import APIRouter, Depends, Query
from fastapi_pagination import Page

from point.auth import get_user
from point.view import AuthUser, ReferralOut, fake

router = APIRouter()


@router.get("s")
async def get_referrals(
        user: AuthUser = Depends(get_user),
        page: int = Query(ge=1, default=1),
        size: int = Query(ge=1, le=100, default=10)
) -> Page[ReferralOut]:
    total_rows = fake.random_int(1, 10000)
    referrals = [ReferralOut(
        name=fake.name(),
        bonus_balance=fake.random_int(10 ** (99 - page), 10 ** (99 - page + 1)),
        icon=fake.image_url(1280, 720),
    ) for _ in range(fake.random_int(1, size))]
    referrals.sort(key=lambda x: x.bonus_balance, reverse=True)
    total_pages = ceil(total_rows / size)

    return Page(total=total_rows, page=page, size=size, items=referrals, pages=total_pages)
