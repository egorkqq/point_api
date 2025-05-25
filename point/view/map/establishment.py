from uuid import UUID

from pydantic import Field

from point.types import ImageUrl
from point.view import PointBase


class EstablishmentOut(PointBase):
    id: UUID
    name: str = Field(max_length=128)
    icon: ImageUrl
