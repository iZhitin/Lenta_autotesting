#!/usr/bin/python3
# -*- encoding=utf8 -*-

# первая строчка позволяет запускать код на разных OS, в случае если интерпретатор установлен в разных локациях
# вторая строка устанавливает кодировку

# для визуального контроля
import time

# импортируем класс тестируемой страницы
from pages.main_page import MainPage

# для запуска тестов через терминал:
# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests\test_main_page.py


def test_main_page(selenium):
    # создаем экземпляр класса тестируемой страницы
    page = MainPage(selenium)
    # открываем главную страницу
    selenium.get(page.url)

    # соглашение с cookie
    page.wait_scroll_and_click_on_element(page.cookie_agree_button)
    # прокликивание стрелочки вправо на первом баннере
    page.wait_and_click_on_one_of_elements(page.right_buttons, 0)
    page.wait_and_click_on_one_of_elements(page.right_buttons, 0)
    page.wait_and_click_on_one_of_elements(page.right_buttons, 0)

    # клик на каталог из предложения в хэдере
    page.wait_scroll_and_click_on_element(page.go_to_catalog_from_ad)

    # идем обратно, НАДО ! реализовать функцию back
    selenium.get(page.url)

    # клик на акционный блок
    page.wait_scroll_and_click_on_element(page.selection_board)
    # как работает переключение между окнами
    selenium.switch_to.window(selenium.window_handles[0])
    # скриншот
    page.take_screenshot()
    time.sleep(5)
