from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_number, wrong_card_number):
    assert get_mask_card_number(1111111111111111) == card_number
    assert get_mask_card_number(1111) == wrong_card_number


def test_get_mask_account(account_number, wrong_account_number):
    assert get_mask_account(11111111111111111111) == account_number
    assert get_mask_account(1111111111) == wrong_account_number
