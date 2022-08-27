"""Файл предназначен для хранения импортов и объектов, чтобы не загромождать код тестов"""
# импортируем необходимые библиотеки

import pytest


# необходимые функции
def russian_chars(n=1):
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' * n


def english_chars(n=1):
    return 'abcdefghijklmnopqrstuvwxyz' * n


def digits(n=1):
    return 1234567890 * n


def generate_string(n=1):
    return "ПоискSearch" * n


def special_chars(n=1):
    return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}' * n


# здесь мы взяли 20 популярных китайских иероглифов
def chinese_chars(n=1):
    return '的一是不了人我在有他这为之大来以个中上们' * n


def empty_space(n=1):
    return " " * n


def everything(n=1):
    return (russian_chars().upper() + russian_chars() + chinese_chars() + special_chars()) * n


# сюда можно попробовать инъекции