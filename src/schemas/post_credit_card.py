from typing import Optional
from datetime import date
from uuid import UUID

from pydantic import BaseModel, Field, root_validator
from creditcard import CreditCard
from creditcard.exceptions import BrandNotFound

from src.services.cryptography import encrypt


class PostCreditCardSchema(BaseModel):
    exp_date: date
    holder: str
    number: str = Field(regex="\d+", max_length=20)
    cvv: Optional[str] = Field(regex="\d+", min_length=3, max_length=4)

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
