#!/usr/bin/python3
# -*- encoding=utf8 -*-

# первая строчка позволяет запускать код на разных OS, в случае если интерпретатор установлен в разных локациях
# вторая строка устанавливает кодировку

# для визуального контроля
import time

# импортируем класс тестируемой страницы
from pages.product_page import ProductPage


# для запуска тестов через терминал:
# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests\test_catalog_page.py

class TestProductPageClass:

    def test_image_magnifying_works(self, selenium):
        # создаем экземпляр класса тестируемой страницы
        page = ProductPage(selenium)
        # открываем страницу
        selenium.get(page.url)
        page.wait_and_scroll_to_element(page.image_in_product_page)
        time.sleep(4)

        assert page.is_presented(page.image_magnifying) is True, "Тег изображения не меняется, что-то пошло не так" \
                                                                 "при наведении курсора мыши для увеличения"
