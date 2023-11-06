from typing import Optional
from datetime import date
from uuid import UUID

from pydantic import BaseModel, Field, root_validator
from creditcard import CreditCard

from src.services.cryptography import encrypt


class PostCreditCardSchema(BaseModel):
    exp_date: date
    holder: str
    number: str = Field(regex="\d+", max_length=20)
    cvv: Optional[str]

    @root_validator()
    def validate_number(cls, values):
        number = values["number"]
        credit_card = CreditCard(number)
        if not credit_card.is_valid():
            raise ValueError("Invalid credit card number")
        values["number"] = encrypt(number)
        return values

class PostCreditCardResponse(BaseModel):
    id: UUID
