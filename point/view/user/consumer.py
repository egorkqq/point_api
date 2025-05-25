from uuid import UUID

from pydantic import Field

from point.types import TonAddress
from point.view import PointBase


class ConsumerMeta(PointBase):
    show_tips_left: bool = False


class ConsumerPublicOut(PointBase):
    id: UUID
    typs_left: int | None = Field(ge=0, default=None)


class ConsumerOut(ConsumerPublicOut):
    wallet: TonAddress
    meta: ConsumerMeta


class ConsumerUpdateIn(PointBase):
    wallet: TonAddress | None = None
    meta: ConsumerMeta | None = None
