from src.models.credit_card import CreditCard
from src.models import Session


class PostCreditCard:
    def __init__(self, session: Session):
        self._session = session

    def create(self, credit_card):
        credit_card_model = CreditCard(
            **credit_card.dict()
        )

        self._session.add(credit_card_model)
        self._session.commit()
        
        return credit_card_model
