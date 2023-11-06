from typing import Union

from fastapi import FastAPI


from src.routes.api_v1_credit_card_viewer import router as api_v1_credit_card

app = FastAPI()

app.include_router(api_v1_credit_card)
