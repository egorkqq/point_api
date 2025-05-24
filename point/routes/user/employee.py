from uuid import UUID, uuid4

from fastapi import APIRouter, Depends

from point.auth import get_user
from point.errors import APIException, ErrorCode
from point.types import UserType
from point.view import EmployeeUpdateIn, EmployeePublicOut, fake, random_address, AuthUser
from point.view.user.user import UserPublicOut

router = APIRouter(tags=["Employee"])


@router.get("/{employee_id}")
async def get(employee_id: UUID, _: AuthUser = Depends(get_user)) -> UserPublicOut:
    return UserPublicOut(
        name=fake.name(),
        username=fake.user_name(),
        rank=fake.random_int(1, 10 ** 10),
        user_type=UserType.employee,
        account=EmployeePublicOut(
            id=employee_id,
            job_place_id=fake.random_element([uuid4(), None]),
            purpose_id=fake.random_element([uuid4(), None]),
            wallet=random_address(),
        )
    )


@router.put("")
async def update(update_in: EmployeeUpdateIn, user: AuthUser = Depends(get_user)) -> None:
    if update_in.id != user.id:
        raise APIException(ErrorCode.ACCESS_FORBIDDEN)

    return None
