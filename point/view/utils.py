import random
from uuid import UUID

from pydantic import Field

from point.types import ImageUrl, TonAddress
from point.view.base import PointBase


class Establishment(PointBase):
    id: UUID
    alias: str = Field(max_length=128)
    icon: ImageUrl


def random_address() -> TonAddress:
    return TonAddress(root=f"0:{random.randbytes(32).hex()}")
