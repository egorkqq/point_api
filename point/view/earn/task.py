from uuid import UUID

from pydantic import Field

from point.view.base import PointBase


class TaskOut(PointBase):
    id: UUID
    title: str = Field(max_length=32)
    description: str = Field(max_length=256)
    profit: int = Field(gt=0)
