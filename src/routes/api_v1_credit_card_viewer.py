from fastapi import APIRouter, Depends
from typing import List
from uuid import UUID

from src.models import get_session, Session

router = APIRouter(prefix="/api/v1/credit-card")

from src.schemas.post_credit_card import PostCreditCardResponse, PostCreditCardSchema
from src.schemas.get_credit_card import GetCreditCardSchema
from src.use_cases.post_credit_card import PostCreditCard
from src.use_cases.get_credit_card import GetCreditCard
from src.use_cases.get_credit_cards import GetCreditCards


@router.get("", response_model=List[GetCreditCardSchema])
def read_credit_cards(session: Session = Depends(get_session)):
    return GetCreditCards(session).list()


@router.get("/{key}", response_model=GetCreditCardSchema)
def read_credit_card(key: UUID, session: Session = Depends(get_session)):
    return GetCreditCard(session).get(key)


@router.post("", status_code=201, response_model=PostCreditCardResponse)
def write_credit_card(body: PostCreditCardSchema, session: Session = Depends(get_session)):
    return PostCreditCard(session).create(body)
