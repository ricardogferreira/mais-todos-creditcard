
from datetime import date

from src.models.credit_card import CreditCard

HEADERS = {"Authorization": "test123"}


def test_post_api_v1_credit_card_required_fields(client):
    response = client.post(
        url="/api/v1/credit-card",
        json={},
        headers=HEADERS,
    )

    response_data = response.json()
    assert response.status_code == 422
    assert response_data["detail"] == [
        {"loc": ["body", "exp_date"], "msg": "field required", "type": "value_error.missing"},
        {"loc": ["body", "holder"], "msg": "field required", "type": "value_error.missing"},
        {"loc": ["body", "number"], "msg": "field required", "type": "value_error.missing"},
        {
            "loc": ["body", "__root__"],
            "msg": "expected string or bytes-like object",
            "type": "type_error",
        },
    ]


def test_post_api_v1_credit_card_success(mocker, client):
    mocker.patch(
        "src.use_cases.post_credit_card.CreditCard",
        return_value=CreditCard(id="58b352f2-2ac5-476d-8e14-027f6d247a08"),
    )
    response = client.post(
        url="/api/v1/credit-card",
        json={
            "exp_date": "2023-11-06",
            "holder": "holder test",
            "number": "4917480000000008",
            "cvv": "5921",
        },
        headers=HEADERS,
    )

    response_data = response.json()
    assert response.status_code == 201
    assert response_data == {"id": "58b352f2-2ac5-476d-8e14-027f6d247a08"}


def test_get_api_v1_credit_card_success(mocker, client):
    mocker.patch(
        "src.use_cases.get_credit_card.CreditCard.list",
        return_value=[
            CreditCard(
                id="58b352f2-2ac5-476d-8e14-027f6d247a08",
                number="gAAAAABlSOmLuuoz8l9KvDcvA6j1xK5a8nXrV7uz9xCZs_9Kzk9uUuwy6QlfPrS62O50Ew8Cz7RpsrQbD161sIRfeBBQ_xpgkHbmQZLKh8ODI5Sf_AWOkAg=",
                brand="visa",
                holder="test",
                exp_date=date(2023, 11, 6),
            )
        ],
    )
    response = client.get(
        url="/api/v1/credit-card",
        headers=HEADERS,
    )

    response_data = response.json()
    assert response.status_code == 200
    assert response_data == []
