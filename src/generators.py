def filter_by_currency(transactions: list[dict], currency: str) -> iter:
    """Принимает список транзакций и возвращает транзакции по заданной валюте"""
    return iter(i for i in transactions if i["operationAmount"]["currency"]["code"] == currency)


def transaction_descriptions(transactions: list[dict]) -> str:
    """Принимает список транзакций и возвращает описание транзакции"""
    # yield (i["description"] for i in transactions if i["description"] != "")
    for i in transactions:
        if i["description"] != "":
            yield i["description"]


def card_number_generator(start, stop):
    """Генерирует номер карты в диапозоне от 0000000000000001 до 999999999999999"""
    for number in range(start, stop):
        card_number = str(number)
        while len(card_number) < 16:
            card_number = "0" + card_number
        formatted_card_number = f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
        yield formatted_card_number
