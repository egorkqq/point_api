from uuid import UUID

from pydantic import Field

from point.types import ImageUrl
from point.view.base import PointBase


class EstablishmentOut(PointBase):
    id: UUID
    description: str = Field(max_length=128)
    icon: ImageUrl
