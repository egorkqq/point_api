from uuid import UUID

from point.types import TonAddress
from point.view.base import PointBase


class EmployeeMeta(PointBase):
    show_job: bool = False
    show_purpose: bool = False


class EmployeePublicOut(PointBase):
    id: UUID
    wallet: TonAddress
    job_place_id: UUID | None = None
    purpose_id: UUID | None = None


class EmployeeOut(EmployeePublicOut):
    job_place_id: UUID
    purpose_id: UUID

    meta: EmployeeMeta


class EmployeeUpdateIn(PointBase):
    id: int
    wallet: TonAddress | None = None
    purpose_id: UUID | None = None
    meta: EmployeeMeta | None = None
