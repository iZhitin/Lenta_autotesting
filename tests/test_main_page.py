#!/usr/bin/python3
# -*- encoding=utf8 -*-

# первая строчка позволяет запускать код на разных OS, в случае если интерпретатор установлен в разных локациях
# вторая строка устанавливает кодировку

# для визуального контроля
import time
# для работы с cookie
import pickle

# импортируем класс тестируемой страницы
from pages.main_page import MainPage

# для запуска тестов через терминал:
# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests\test_main_page.py


def test_main_page(selenium):
    # создаем экземпляр класса тестируемой страницы
    page = MainPage(selenium)

    page.get_url(page.url)


    # клик на акционный блок
    # page.scroll_wait_and_click_on_element(page.selection)
    # клик на каталог из предложения в хэдере
    page.scroll_wait_and_click_on_element(page.go_to_catalog_from_ad)
    # как работает переключение между окнами
    # selenium.switch_to.window(selenium.window_handles[0])
    # клик на категорию мясо, птица, колбаса
    page.scroll_wait_and_click_on_element(page.meat_category)

#     with open("my_cookies.txt", "wb") as cookies:
# #         pickle.dump(selenium.get_cookies(), cookies)



