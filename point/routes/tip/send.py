import base64

from fastapi import APIRouter
from fastapi.params import Depends

from point.auth import get_user
from point.view import AuthUser, CheckoutTransferIn, CheckoutTransferOut, random_address, fake

router = APIRouter()


@router.post("/checkout")
async def checkout_transfer(checkout_in: CheckoutTransferIn, user: AuthUser = Depends(get_user)) -> CheckoutTransferOut:
    return CheckoutTransferOut(
        to=random_address(),
        value=fake.random_int(1, 10 ** 10),
        body=base64.urlsafe_b64encode(fake.text().encode("utf8")).decode("utf8"),
    )
