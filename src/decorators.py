# -*- coding: utf-8 -*-


import time
from functools import wraps
from typing import Any, Optional


def log(filename: Optional[str] = None) -> Any:
    """Декоратор создает файл с логами времени начала и завершения работы функции, а также результата ее работы.
    Если filename не задан, результат логирования выводится в консоль"""

    def logging(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:

            try:
                if filename:
                    time_1 = time.asctime()
                    func_execution = func(*args, **kwargs)
                    time_2 = time.asctime()
                    result = (
                        f"Время начала выполнения функции {func.__name__}: {str(time_1)}."
                        f"\nВремя завершения работы функции {func.__name__}: {str(time_2)}."
                        f"\nРезультат выполнения функции:{func_execution}."
                    )
                    with open(filename, "w") as file:
                        file.write(result)
                elif filename == None:
                    time_1 = time.asctime()
                    func_execution = func(*args, **kwargs)
                    time_2 = time.asctime()
                    result = (
                        f"Время начала выполнения функции {func.__name__}: {str(time_1)}."
                        f"\nВремя завершения работы функции {func.__name__}: {str(time_2)}."
                        f"\nРезультат выполнения функции:{func_execution}."
                    )
                    print(result)
                    return result

            except Exception as e:
                error_message = f"Возникла ошибка {e.__class__.__name__} при выполнении функции {func.__name__}\n"
                if filename:
                    with open(filename, "w") as file:
                        file.write(error_message)
                else:
                    print(error_message)


        return wrapper

    return logging
