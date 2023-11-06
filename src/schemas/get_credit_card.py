from uuid import UUID
from typing import Optional
from datetime import date

from pydantic import BaseModel


class GetCreditCardSchema(BaseModel):
    id: UUID
    exp_date: date
    holder: str
    number: str
    cvv: Optional[str]
    brand: str
