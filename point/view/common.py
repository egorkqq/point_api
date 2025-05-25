from decimal import Decimal
from typing import Self

from pydantic import Field, model_validator

from point.view import PointBase


class PointIn(PointBase):
    latitude: Decimal = Field(ge=-90, le=90)
    longitude: Decimal = Field(ge=-180, le=180)


class PointOut(PointIn):
    address: str = Field(max_length=128)


class PointPair(PointBase):
    upper: PointIn
    lower: PointIn

    @model_validator(mode="after")
    def validate_model(self) -> Self:
        if self.upper.longitude < self.lower.longitude or self.upper.latitude < self.lower.latitude:
            raise ValueError("Upper point must be bigger than lower point")

        return self
