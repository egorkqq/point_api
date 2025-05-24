from uuid import UUID

from pydantic import Field
from point.view.base import PointBase


class TaskOut(PointBase):
    id: UUID
    title: str = Field(max_length=128)
    description: str = Field(max_length=512)
    profit: int = Field(ge=0)
