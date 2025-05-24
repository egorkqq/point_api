from uuid import UUID

from pydantic import Field

from point.types import ImageUrl
from point.view.base import PointBase


class Creator(PointBase):
    name: str = Field(max_length=32)
    icon: ImageUrl


class MainPlace(PointBase):
    name: str = Field(max_length=64)
    description: str = Field(max_length=256)
    icons: list[ImageUrl] = Field(default_factory=list)


class SelectionPreview(PointBase):
    id: UUID
    creator: Creator
    main_area: str = Field(max_length=32)
    main_place: MainPlace
    places_count: int = Field(default=0, ge=0)
    preview_places_icons: list[ImageUrl] = Field(default_factory=list)


class PlaceItem(PointBase):
    id: UUID
    name: str = Field(max_length=64)
    description: str = Field(max_length=256)
    icon: ImageUrl
    address: str = Field(max_length=64)


class SelectionOut(PointBase):
    id: UUID
    creator: Creator
    main_area: str = Field(max_length=32)
    places: list[PlaceItem] = Field(default_factory=list)
