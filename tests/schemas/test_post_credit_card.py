import pytest
from src.schemas.post_credit_card import PostCreditCardSchema


@pytest.mark.parametrize(
    "value,error_message",
    [("13/2022", "Invalid month: 13"), ("aa", "Invalid date"), ("09/2023", "Credit card Expired")],
)
def test_validate_exp_date_raises_value_error(value, error_message):
    values = {"exp_date": value}
    with pytest.raises(ValueError, match=error_message):
        PostCreditCardSchema.validate_exp_date(values)


def test_validate_number_and_set_brand_raises_value_error():
    values = {"number": "123231312"}
    with pytest.raises(ValueError, match="Invalid credit card number"):
        PostCreditCardSchema.validate_number_and_set_brand(values)
