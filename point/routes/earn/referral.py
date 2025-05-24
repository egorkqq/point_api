from fastapi import APIRouter, Depends

from point.auth import get_user
from point.view import AuthUser, ReferralOut, fake

router = APIRouter()


@router.get("s")
async def get_referrals(user: AuthUser = Depends(get_user)) -> list[ReferralOut]:
    referrals = [ReferralOut(
        name=fake.name(),
        bonus_balance=fake.random_int(1, 10 ** 10),
        icon=fake.image_url(),
    ) for _ in range(fake.random_int(1, 10))]
    referrals.sort(key=lambda x: x.bonus_balance, reverse=True)
    return referrals
