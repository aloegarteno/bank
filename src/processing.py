from typing import Any, Iterable


def filter_by_state(list_of_operations: list[dict[str, Any]], default_state: Any = "EXECUTED") -> list[dict[str, Any]]:
    """Принимает список операций и возвращает только выполненные операции"""
    executed_operations = list()
    for operation_status in list_of_operations:
        if operation_status.get("state") == default_state:
            executed_operations.append(operation_status)
    return executed_operations


def sort_by_date(list_of_dicts: Iterable[list], reverse_list: bool = True) -> Iterable[list]:
    """Принимает список словарей операций и возвращает отсортированный список операций(По умолчанию - убывание)"""
    return sorted(list_of_dicts, key=lambda x: x["date"], reverse=reverse_list)
