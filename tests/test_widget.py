import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Счет 11111111111111111111", "Счет **1111"),
        ("Master Card 2674857491027564", "Master Card 2674 85** **** 7564"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("7000792289606361", "7000 79** **** 6361"),
    ],
)


def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-12-15", "15.12.2024"),
        ("2024.01.22", "22.01.2024"),
        ("", "Неверная дата"),
    ],
)


def test_get_date(value, expected):
    assert get_date(value) == expected
