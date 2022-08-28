#!/usr/bin/python3
# -*- encoding=utf8 -*-

# первая строчка позволяет запускать код на разных OS, в случае если интерпретатор установлен в разных локациях
# вторая строка устанавливает кодировку

# для визуального контроля (в некоторых случаях, для ожидания загрузки страницы)
import time

# импортируем класс тестируемой страницы
from pages.product_page import ProductPage

# для маркировки тестов
import pytest


@pytest.mark.product_page
@pytest.mark.fast
@pytest.mark.feature
def test_image_magnifying_works(selenium):
    """Появление окна с увеличенным изображением при наведении мыши на фото товара."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = ProductPage(selenium)
    selenium.get(page.url)

    page.wait_and_scroll_to_element(page.image_in_product_page)
    time.sleep(1)

    assert page.is_presented(page.image_magnifying) is True, "Тег изображения не меняется, что-то пошло не так" \
                                                             "при наведении курсора мыши для увеличения"
