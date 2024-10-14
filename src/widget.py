from masks import get_mask_account
from masks import get_mask_card_number


def mask_account_card(card_info: str) -> str:
    if 'Счет' in card_info:
        return f'Счет {get_mask_account(int(card_info[4:]))}'
    else:
        return card_info[0:-16] + get_mask_card_number(card_info[-16:])
