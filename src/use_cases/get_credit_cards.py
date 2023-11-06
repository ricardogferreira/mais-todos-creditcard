from typing import Dict

from src.models.credit_card import CreditCard
from src.models import Session


class GetCreditCards:
    def __init__(self, session: Session):
        self._session = session

    def list(self, filters: Dict = dict()):
        return CreditCard.list(self._session, **filters)
