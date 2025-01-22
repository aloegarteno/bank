import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(transactions_list, usd_transactions):
    result = filter_by_currency(transactions_list, "USD")
    assert (next(result)) == usd_transactions


def test_filter_by_currency_rub(transactions_list, rub_transactions):
    result = filter_by_currency(transactions_list, "RUB")
    assert next(result) == rub_transactions


def test_transaction_descriptions(transactions_list, operation_descriptions):
    assert list(transaction_descriptions(transactions_list)) == operation_descriptions


@pytest.mark.parametrize(
    "value_1, value_2,  expected",
    [(1, 4, "0000 0000 0000 0001"), (2, 4, "0000 0000 0000 0002"), (3, 4, "0000 0000 0000 0003")],
)
def test_card_number_generator_min(value_1, value_2, expected):
    generator = card_number_generator(value_1, value_2)
    assert next(generator) == expected


@pytest.mark.parametrize(
    "value_1, value_2,  expected",
    [
        (9999999999999997, 9999999999999999, "9999 9999 9999 9997"),
        (9999999999999998, 9999999999999999, "9999 9999 9999 9998"),
    ],
)
def test_card_number_generator_max(value_1, value_2, expected):
    generator = card_number_generator(value_1, value_2)
    assert next(generator) == expected
