from typing import Self

from pydantic import Field, model_validator

from point.types import UserType, ImageUrl
from point.view import PointBase

from . import EmployeeOut, ConsumerOut, EmployeePublicOut, ConsumerPublicOut


class AuthUserIn(PointBase):
    id: int = Field(default=None)
    first_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    username: str | None = Field(default=None)
    language_code: str | None = Field(default=None)
    photo_url: ImageUrl | None = Field(default=None)
    is_bot: bool | None = Field(default=None)
    is_premium: bool | None = Field(default=None)
    allows_write_to_pm: bool | None = Field(default=None)


class AuthUserOut(AuthUserIn):
    rank: int
    bonus_balance: int = 0
    user_type: UserType
    account: EmployeeOut | ConsumerOut

    @model_validator(mode="after")
    def validate_model(self) -> Self:
        if (
                self.user_type == UserType.consumer and not isinstance(self.account, ConsumerOut) or
                self.user_type == UserType.employee and not isinstance(self.account, EmployeeOut)
        ):
            raise ValueError("Mismatch user type and account model")
        return self


class AuthUser(PointBase):
    id: int
    username: str | None = Field(default=None)
    sessionId: str | None = Field(default=None)


class UserPublicOut(PointBase):
    name: str
    username: str
    rank: int
    user_type: UserType
    account: EmployeePublicOut | ConsumerPublicOut
