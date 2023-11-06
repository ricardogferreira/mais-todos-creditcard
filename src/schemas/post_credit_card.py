import calendar
from calendar import IllegalMonthError
import re
from typing import Optional
from datetime import date
from uuid import UUID

from pydantic import BaseModel, Field, root_validator
from creditcard import CreditCard
from creditcard.exceptions import BrandNotFound

from src.services.cryptography import encrypt


class PostCreditCardSchema(BaseModel):
    exp_date: str = Field(min_length=7, max_length=7, regex="^\d{2}/\\d{4}$")
    holder: str = Field(min_length=3)
    number: str = Field(regex="\d+", max_length=20)
    cvv: Optional[str] = Field(regex="\d+", min_length=3, max_length=4)

    @classmethod
    def _validate_number_mask(cls, value):
        pattern = "^\d{2}/\\d{4}$"
        return bool(re.match(pattern, value))

    @classmethod
    def _mount_date(cls, value):
        month, year = value.split("/")
        month, year = int(month), int(year)
        try:
            day = calendar.monthrange(year, month)[-1]
        except IllegalMonthError as exc:
            raise ValueError(f"Invalid month: {exc.month}") from exc
        return date(year, month, day)

    @root_validator(pre=False)
    def validate_exp_date(cls, values):
        exp_date = values.get("exp_date")
        if exp_date and cls._validate_number_mask(exp_date):
            exp_date = cls._mount_date(exp_date)
            if exp_date < date.today():
                raise ValueError("Credit card Expired")
            values["exp_date"] = exp_date.isoformat()
        else:
            raise ValueError("Invalid date")
        return values

    @root_validator()
    def validate_number_and_set_brand(cls, values):
        number = values.get("number")
        credit_card = CreditCard(number)
        if not credit_card.is_valid():
            raise ValueError("Invalid credit card number")
        values["number"] = encrypt(number)
        try:
            values["brand"] = credit_card.get_brand()
        except BrandNotFound:
            raise ValueError("Brand not found")
        return values


class PostCreditCardResponse(BaseModel):
    id: UUID
