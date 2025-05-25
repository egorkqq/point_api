from pydantic import Field

from point.types import ImageUrl
from point.view import PointBase


class ReferralOut(PointBase):
    name: str = Field(max_length=32)
    bonus_balance: int = 0
    icon: ImageUrl
