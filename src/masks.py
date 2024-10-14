def get_mask_card_number(card_number: int) -> str:
    """Принимает номер карты и возвращает его маску в виде: 1111 11** ****1111"""
    str_card_number = str(card_number)

    return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"


def get_mask_account(account_number: int) -> str:
    """Принимает номер счета и возвращает его маску в виде: **1111"""
    str_account_number = str(account_number)

    return f"**{str_account_number[-4:]}"
