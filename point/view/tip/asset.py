from pydantic import Field

from point.types import ImageUrl, TonAddress
from point.view.base import PointBase


class AssetOut(PointBase):
    name: str = Field(max_length=32)
    ticker: str = Field(max_length=16)
    address: TonAddress
    icon: ImageUrl
    # todo?: balance
