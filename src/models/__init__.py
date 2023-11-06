from sqlalchemy.orm import scoped_session, sessionmaker
from sqlmodel import Session, create_engine

from src.settings import POSTGRES_CONNECTION_URL

Session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        expire_on_commit=False,
        bind=create_engine(
            url=POSTGRES_CONNECTION_URL, pool_size=10, pool_recycle=60, max_overflow=0, echo=False
        ),
    )
)


def get_session():
    with Session() as session:
        yield session
