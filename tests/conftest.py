import pytest


@pytest.fixture
def card_number():
    return "1111 11** **** 1111"


@pytest.fixture
def wrong_card_number():
    return "Неверный номер карты"


@pytest.fixture
def account_number():
    return "**1111"


@pytest.fixture
def wrong_account_number():
    return "Неверный номер счета"