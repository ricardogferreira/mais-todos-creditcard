from typing import Optional
from uuid import UUID, uuid4
from datetime import date

from sqlmodel import Field, SQLModel

from src.models import Session


class CreditCard(SQLModel, table=True):
    __tablename__ = "credit_card"
    id: Optional[UUID] = Field(
        primary_key=True,
        default_factory=uuid4,
        index=True,
        nullable=False,
    )
    exp_date: date
    holder: str
    number: str
    cvv: Optional[str]

    @classmethod
    def get(cls, session: Session, id: UUID):
        return session.query(cls).get(id)

    @classmethod
    def list(cls, session: Session, **kwargs):
        return session.query(cls).filter_by(**kwargs).all()
