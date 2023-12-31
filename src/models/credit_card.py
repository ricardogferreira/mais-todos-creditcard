from typing import Optional
from uuid import UUID, uuid4
from datetime import date

from sqlmodel import Field, SQLModel

from src.models import Session
from src.services.cryptography import decrypt


class CreditCard(SQLModel, table=True):
    __tablename__ = "credit_card"
    id: Optional[UUID] = Field(
        primary_key=True,
        default_factory=uuid4,
        index=True,
        nullable=False,
    )
    exp_date: date
    holder: str = Field(min_length=3)
    number: str
    cvv: Optional[str] = Field(min_length=3, max_length=4)
    brand: str

    @classmethod
    def get(cls, session: Session, id: UUID):
        return session.query(cls).get(id)

    @classmethod
    def list(cls, session: Session, **kwargs):
        return session.query(cls).filter_by(**kwargs).all()

    @property
    def number_decrypted(self):
        if self.number:
            return decrypt(self.number)
