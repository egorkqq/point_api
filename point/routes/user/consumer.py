from uuid import UUID, uuid4

from fastapi import APIRouter, Depends

from point.auth import get_user
from point.types import UserType
from point.view import (
    AuthUser,
    UserPublicOut,
    ConsumerPublicOut,
    ConsumerMeta,
    ConsumerUpdateIn,
    ConsumerOut,
    AuthUserOut,
    fake,
    random_address
)

router = APIRouter(tags=["Consumer"])


@router.get("/{consumer_id}")
async def get(consumer_id: UUID, _: AuthUser = Depends(get_user)) -> UserPublicOut:
    return UserPublicOut(
        name=fake.name(),
        username=fake.user_name(),
        rank=fake.random_int(1, 10 ** 10),
        user_type=UserType.employee,
        account=ConsumerPublicOut(
            id=consumer_id,
            typs_left=fake.random_choices([None, fake.random_int(1, 10 ** 10)]),
        )
    )


@router.put("")
async def update(update_in: ConsumerUpdateIn, user: AuthUser = Depends(get_user)) -> AuthUserOut:
    return AuthUserOut(
        id=user.id,
        username=user.username,
        rank=fake.random_int(1, 10 ** 10),
        bonus_balance=fake.random_int(1, 10 ** 10),
        user_type=UserType.consumer,
        account=ConsumerOut(
            id=uuid4(),
            typs_left=fake.random_int(1, 10 ** 10),
            wallet=random_address() if update_in.wallet is None else update_in.wallet,
            meta=ConsumerMeta(show_tips_left=fake.boolean()) if update_in.meta is None else update_in.meta,
        )
    )
