import random
from decimal import Decimal

from point.types import TonAddress
from point.view import PointIn


def random_address() -> TonAddress:
    return TonAddress(root=f"0:{random.randbytes(32).hex()}")


def point_distance(point1: PointIn, point2: PointIn) -> Decimal:
    return (
            (point1.latitude - point2.latitude) ** 2 +
            (point1.longitude - point2.longitude) ** 2
    ).sqrt()
