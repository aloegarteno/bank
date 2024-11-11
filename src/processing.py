from typing import Any, Iterable


def filter_by_state(list_of_operations: Iterable[list], default_state: Any = "EXECUTED") -> Iterable[list]:
    """Принимает список операций и возвращает только выполненные операции"""
    executed_operations = list()
    for operation_status in list_of_operations:
        if operation_status.get("state") == default_state:
            executed_operations.append(operation_status)
    return executed_operations
