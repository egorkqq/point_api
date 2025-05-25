from decimal import Decimal
from uuid import UUID

from pydantic import Field, AnyUrl

from point.types import ImageUrl
from point.view import PointBase, PointOut, PointIn


class PlacePreview(PointBase):
    id: UUID
    name: str = Field(max_length=128)
    photo: ImageUrl
    establishment_id: UUID
    position: PointOut
    rating: Decimal = Field(ge=0)


class Cost(PointBase):
    value: Decimal = Field(ge=0)
    currency: str = Field(max_length=8)


class MenuItem(PointBase):
    title: str = Field(max_length=128)
    description: str = Field(max_length=512)
    photo: ImageUrl
    cost: Cost


class NearPlaceCriteria(PointBase):
    name: str | None = Field(max_length=128)
    location: PointIn


class PlaceOut(PlacePreview):
    description: str = Field(max_length=512)
    user_rating: int | None = Field(default=None, ge=0, le=5)
    channel_link: AnyUrl | None = Field(default=None, max_length=512)
    icon: ImageUrl
    gallery: list[ImageUrl] = Field(default_factory=list)
    menu: list[MenuItem] = Field(default_factory=list)
