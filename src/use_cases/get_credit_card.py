from uuid import UUID

from src.models.credit_card import CreditCard
from fastapi import HTTPException

from src.models import Session


class GetCreditCard:
    def __init__(self, session: Session):
        self._session = session

    def get(self, id: UUID):
        credit_card = CreditCard.get(self._session, id)
        if credit_card:
            return credit_card
        raise HTTPException(status_code=404, detail="Credit card not found")
