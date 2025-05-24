from decimal import Decimal
from uuid import UUID

from pydantic import Field

from point.types import ImageUrl
from point.view.base import PointBase

from .common import Point


class PlacePreview(PointBase):
    id: UUID
    name: str = Field(max_length=128)
    photo: ImageUrl
    establishment_id: UUID
    position: Point
    rating: Decimal = Field(ge=0)


class Cost(PointBase):
    value: Decimal = Field(ge=0)
    currency: str = Field(max_length=8)


class MenuItem(PointBase):
    title: str = Field(max_length=128)
    description: str = Field(max_length=512)
    photo: ImageUrl
    cost: Cost


class PlaceOut(PlacePreview):
    description: str = Field(max_length=512)
    icon: ImageUrl
    gallery: list[ImageUrl] = Field(default_factory=list)
    menu: list[MenuItem] = Field(default_factory=list)
