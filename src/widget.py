from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info: str) -> str:
    """Принимает строку с названием и номером карты или номер счета и возвращает маску карты или счета"""
    if "Счет" in card_info:
        return f"Счет {get_mask_account(int(card_info[4:]))}"
    else:
        return str(card_info[0:-16] + get_mask_card_number(card_info[-16:]))


def get_date(date: str) -> str:
    """Принимает строку с датой и возвращает ее в формате ДД.ММ.ГГГГ"""
    if len(date) != 0:
        return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
    else:
        return "Неверная дата"
