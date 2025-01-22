# -*- coding: utf-8 -*-

import time

from src.decorators import log


@log()
def summ(a, b):
    return a + b


@log(filename="logs.txt")
def divide(a, b):
    return a / b


def test_log_console(capsys):
    summ(1, 2)
    captured = capsys.readouterr()
    assert (f"Время начала выполнения функции summ: {time.asctime()}.\n"
            f"Время завершения работы функции summ: {time.asctime()}.\n"
            f"Результат выполнения функции:3.") in captured.out


def test_log_console_error(capsys):
    summ(1, "2")
    captured = capsys.readouterr()
    assert "Возникла ошибка TypeError при выполнении функции summ" in captured.out


def test_log():
    divide(10, 2)
    with open("logs.txt", "r") as file:
        result = file.read()
    assert result == (
        f"Время начала выполнения функции divide: {time.asctime()}.\n"
        f"Время завершения работы функции divide: {time.asctime()}.\n"
        f"Результат выполнения функции:5.0."
    )


def test_log_error():
    divide(10, 0)
    with open("logs.txt", "r") as file:
        result = file.read()
    assert result == "Возникла ошибка ZeroDivisionError при выполнении функции divide\n"
