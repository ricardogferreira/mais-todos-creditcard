from src.models.credit_card import CreditCard

HEADERS = {"Authorization": "test123"}


def test_post_api_v1_credit_card_required_fields(client, session):
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
        {"loc": ["body", "__root__"], "msg": "Invalid date", "type": "value_error"},
        {
            "loc": ["body", "__root__"],
            "msg": "expected string or bytes-like object",
            "type": "type_error",
        },
    ]


def test_post_api_v1_credit_card_success(client, session):
    response = client.post(
        url="/api/v1/credit-card",
        json={
            "exp_date": "11/2023",
            "holder": "holder test",
            "number": "4917480000000008",
            "cvv": "5921",
        },
        headers=HEADERS,
    )

    response_data = response.json()
    assert response.status_code == 201
    credit_card = session.query(CreditCard).get(response_data["id"])
    assert response_data["id"] == str(credit_card.id)
