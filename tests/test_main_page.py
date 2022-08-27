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

# import pytest
# @pytest.mark.main_page
# # ModuleNotFoundError: No module named 'pages'


# попытки вынести создание экземпляра в самое начало, чтобы не дублировать в каждом тесте
# PytestCollectionWarning: cannot collect test class 'TestClass' because it has a __init__ constructor (from: tests/test_main_page.py)
# class TestClass:
#     def __init__(self, selenium):
#         self.selenium = selenium
#         self.p = MainPage(selenium)

class TestMainPageClass:

    def ttest_not_to_ask_cookie_twice(self, selenium):
        # создаем экземпляр класса тестируемой страницы
        page = MainPage(selenium)
        # открываем главную страницу
        selenium.get(page.url)
        # соглашение с cookie
        page.wait_scroll_and_click_on_element(page.cookie_agree_button)
        selenium.refresh()
        time.sleep(2)

        # проверка наличия кнопки после перезагрузки
        flag = None
        try:
            selenium.find_element(*page.cookie_agree_button)
        except:
            flag = False
            # raise selenium.common.exceptions.NoSuchElementException

        assert flag is False, "После соглашения с cookie и" \
                              "перезагрузки, они запрашиваются" \
                              "снова"

    def ttest_banner_buttons(self, selenium):
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
        page.wait_and_click_on_one_of_elements(page.right_buttons, 0)
        # возвращения от последнего элемента к первому правой кнопкой
        page.wait_and_click_on_one_of_elements(page.right_buttons, 0)

        # наоборот: с первого на последний и с последнего на предпоследний
        page.wait_and_click_on_one_of_elements(page.left_buttons, 0)
        page.wait_and_click_on_one_of_elements(page.left_buttons, 0)

    def ttest_banner_clickable(self, selenium):
        # создаем экземпляр класса тестируемой страницы
        page = MainPage(selenium)
        # открываем главную страницу
        selenium.get(page.url)
        # соглашение с cookie
        page.wait_scroll_and_click_on_element(page.cookie_agree_button)

        # клик на акционный акцию в баннер, которая появляется не сразу
        page.wait_scroll_and_click_on_element(page.selection_board)
        # переключение на страницу с открывшейся акцией
        page.switch_tab(1)
        # скриншот
        page.take_screenshot()

    def ttest_banner_in_header_clickable(self, selenium):
        # создаем экземпляр класса тестируемой страницы
        page = MainPage(selenium)
        # открываем главную страницу
        selenium.get(page.url)
        before = selenium.current_url
        # соглашение с cookie
        page.wait_scroll_and_click_on_element(page.cookie_agree_button)
        # клик на каталог из предложения в хэдере
        page.wait_scroll_and_click_on_element(page.go_to_catalog_from_ad)

        # проверка перехода на другую страницу
        after = selenium.current_url

        assert before != after \
               and after == 'https://lenta.com/catalog/?utm_source=lweb&utm_medium=banner&utm_campaign=up', \
                            "Открылась неожиданная страница или переход не осуществлен вовсе"


    def ttest_header_logo_icon_clickable(self, selenium):
        # создаем экземпляр класса тестируемой страницы
        page = MainPage(selenium)
        # открываем главную страницу
        selenium.get(page.url)
        page.wait_scroll_and_click_on_element(page.profile_icon)
        selenium.find_element(*page.header_logo).click()
        time.sleep(5)
        assert selenium.current_url == 'https://lenta.com/', "Переход на главную страницу не осуществляется"

    def ttest_header_search_icon_clickable(self, selenium):
        # создаем экземпляр класса тестируемой страницы
        page = MainPage(selenium)
        # открываем главную страницу
        selenium.get(page.url)
        page.wait_scroll_and_click_on_element(page.search_icon)

    def ttest_header_profile_icon_clickable(self, selenium):
        # создаем экземпляр класса тестируемой страницы
        page = MainPage(selenium)
        # открываем главную страницу
        selenium.get(page.url)
        page.wait_scroll_and_click_on_element(page.profile_icon)

    def ttest_header_liked_icon_clickable(self, selenium):
        # создаем экземпляр класса тестируемой страницы
        page = MainPage(selenium)
        # открываем главную страницу
        selenium.get(page.url)
        page.wait_scroll_and_click_on_element(page.liked_icon)

    def ttest_header_cart_icon_clickable(self, selenium):
        # создаем экземпляр класса тестируемой страницы
        page = MainPage(selenium)
        # открываем главную страницу
        selenium.get(page.url)
        page.wait_scroll_and_click_on_element(page.cart_icon)

    def test_search_field(self, selenium):
        # создаем экземпляр класса тестируемой страницы
        page = MainPage(selenium)
        # установим размер окна (разрешение меняется тоже), чтобы нужный элемент был на странице
        selenium.set_window_size(1035, 768)
        # открываем главную страницу
        selenium.get(page.url)
        # соглашение с cookie
        page.wait_scroll_and_click_on_element(page.cookie_agree_button)

        # обращение к поисковому полю, ввод и нажатие кнопки поиск
        page.wait_scroll_and_click_on_element(page.search_field)
        page.enter_text(page.search_field, 'капуста')
        page.wait_scroll_and_click_on_element(page.search_icon_button)

        assert page.is_presented(page.search_results) is True, "На странице нет элемента с фразой " \
                                                               "'Результаты поиска'"


