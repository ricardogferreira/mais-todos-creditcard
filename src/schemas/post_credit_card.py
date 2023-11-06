from typing import Optional
from datetime import date
from uuid import UUID

from pydantic import BaseModel


class PostCreditCardSchema(BaseModel):
    exp_date: date
    holder: str
    number: str
    cvv: Optional[str]


class PostCreditCardResponse(BaseModel):
    id: UUID
