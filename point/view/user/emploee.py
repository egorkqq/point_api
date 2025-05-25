from uuid import UUID

from pydantic import Field

from point.types import TonAddress, ImageUrl
from point.view import PointBase


class JobPlaceOut(PointBase):
    id: UUID
    name: str = Field(max_length=32)
    address: str = Field(max_length=64)


class PurposeIn(PointBase):
    icon: ImageUrl
    title: str = Field(max_length=32)
    description: str = Field(max_length=512)


class PurposeOut(PurposeIn):
    id: UUID


class EmployeeMeta(PointBase):
    show_job: bool = False
    show_purpose: bool = False


class EmployeePublicOut(PointBase):
    id: UUID
    wallet: TonAddress
    job_place: JobPlaceOut | None = None
    purpose: PurposeOut | None = None


class EmployeeOut(EmployeePublicOut):
    meta: EmployeeMeta


class EmployeeUpdateIn(PointBase):
    wallet: TonAddress | None = None
    purpose: PurposeIn | None = None
    meta: EmployeeMeta | None = None
