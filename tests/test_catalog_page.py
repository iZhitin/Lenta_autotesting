#!/usr/bin/python3
# -*- encoding=utf8 -*-

# первая строчка позволяет запускать код на разных OS, в случае если интерпретатор установлен в разных локациях
# вторая строка устанавливает кодировку

# для визуального контроля
import time

# импортируем класс тестируемой страницы
from pages.catalog_page import CatalogPage

# для запуска тестов через терминал:
# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests\test_catalog_page.py


def test_catalog_page(selenium):
    # создаем экземпляр класса тестируемой страницы
    page = CatalogPage(selenium)
    # page.url - url из класса CatalogPage
    selenium.get(page.url)
    # соглашение с cookie
    page.wait_scroll_and_click_on_element(page.cookie_agree_button)

    # клик на категорию "мясо, птица, колбаса"
    page.wait_scroll_and_click_on_element(page.meat_category)
    time.sleep(3)

    # если использовать цикл for с i, то элементы будут перебираться через один, так как локаторов становится меньше
    # добавления каждого элемента на странице
    count = 23
    while True:
        page.wait_scroll_and_click_on_one_of_elements(page.add_to_busket_button, 0)
        time.sleep(1)
        count -= 1
        if count == 0:
            break

    selenium.refresh()
    time.sleep(3)
    # без * будет ошибка InvalidArgumentException: Message: invalid argument: 'using' must be a string
    assert selenium.find_element(*page.amount_of_goods).text == "23", "Не все товары добавлены в корзину"
