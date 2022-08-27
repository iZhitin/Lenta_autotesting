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

class TestCatalogPageClass:

    def ttest_all_goods_can_be_added_to_busket_from_meat_category_page(self, selenium):
        # Проверка того, что все продукты могут быть добавлены в корзину
        # на первой странице категории "мясо, птица, колбаса"
        # Для тестирования другой категории, нужно просто поменять одну переменную

        # создаем экземпляр класса тестируемой страницы
        page = CatalogPage(selenium)
        # page.url - url из класса CatalogPage
        selenium.get(page.url)
        # соглашение с cookie
        page.wait_scroll_and_click_on_element(page.cookie_agree_button)

        # клик на категорию "мясо, птица, колбаса"
        page.wait_scroll_and_click_on_element(page.meat_category)
        # page.wait_scroll_and_click_on_element(page.meat_category)
        time.sleep(3)

        # если использовать цикл for с i, то элементы будут перебираться через один, так как локаторов становится меньше
        # добавление каждого элемента на странице в корзину
        # количество элементов
        amount_of_elements = len(selenium.find_elements(*page.add_to_busket_button))
        count = int(amount_of_elements)
        while True:
            page.wait_scroll_and_click_on_one_of_elements(page.add_to_busket_button, 0)
            time.sleep(1)
            count -= 1
            if count == 0:
                break

        selenium.refresh()
        time.sleep(2)
        # без * будет ошибка InvalidArgumentException: Message: invalid argument: 'using' must be a string
        assert selenium.find_element(*page.amount_of_goods).text == str(
            amount_of_elements), "Не все товары добавлены в корзину"

    # AttributeError: 'TestCatalogPageClass' object has no attribute 'implicitly_wait' в BasePage, если без self
    def ttest_all_categories_clickable(self, selenium):
        # создаем экземпляр класса тестируемой страницы
        page = CatalogPage(selenium)
        # page.url - url из класса CatalogPage
        selenium.get(page.url)
        # соглашение с cookie
        page.wait_scroll_and_click_on_element(page.cookie_agree_button)

        # список с категориями из каталога
        category_list = [
            page.meat_category,
            page.fruits_and_veg_category,
            page.bakery_category,
            page.hot_beverages_category,
            page.grocery_category,
            page.frozen_category,
            page.milky_and_eggs_category,
            page.seafood_category,
            page.healthy_food_category,
            page.own_food_category,
            page.soft_drinks_category,
            page.alcohol_category,
            page.bread_category,
            page.beauty_and_health_category,
            page.household_chemicals_category,
            page.sport_category,
            page.for_pets_category,
            page.zoomarket_category,
            page.for_cars_category,
            page.appliances_category,
            page.dacha_category,
            page.for_kids_category,
            page.for_home_category,
            page.utensils_category,
            page.clothes_category,
            page.office_category,
            page.textile_category,
            page.flowers_category,
            page.tobacco_category
        ]

        url_before = selenium.current_url
        # прокликивание каждой категории из каталога
        for i in range(len(category_list)):
            page.wait_scroll_and_click_on_element(category_list[i])
            url_after = selenium.current_url
            page.go_back()
            time.sleep(3)
            assert url_before != url_after, "Переход на другую страницу не осуществлен"
