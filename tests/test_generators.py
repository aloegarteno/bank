from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(transactions_list, usd_transactions):
    result = filter_by_currency(transactions_list, "USD")
    assert (next(result)) == usd_transactions


def test_filter_by_currency_rub(transactions_list, rub_transactions):
    result = filter_by_currency(transactions_list, "RUB")
    assert next(result) == rub_transactions


def test_transaction_descriptions(transactions_list, operation_descriptions):
    assert list(transaction_descriptions(transactions_list)) == operation_descriptions


def test_card_number_generator_min():
    generator = card_number_generator(1, 4)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"


def test_card_number_generator_max():
    generator = card_number_generator(9999999999999997, 9999999999999999)
    assert next(generator) == "9999 9999 9999 9997"
    assert next(generator) == "9999 9999 9999 9998"
