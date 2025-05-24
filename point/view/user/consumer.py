from uuid import UUID

from pydantic import Field

from point.view.base import PointBase


class ConsumerMeta(PointBase):
    show_tips_left: bool = False


class ConsumerPublicOut(PointBase):
    id: UUID
    typs_left: int | None = Field(ge=0, default=None)


class ConsumerOut(ConsumerPublicOut):
    meta: ConsumerMeta
