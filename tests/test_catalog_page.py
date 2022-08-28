#!/usr/bin/python3
# -*- encoding=utf8 -*-

# первая строчка позволяет запускать код на разных OS, в случае если интерпретатор установлен в разных локациях
# вторая строка устанавливает кодировку

# для визуального контроля (в некоторых случаях, для ожидания загрузки страницы)
import time

# импортируем класс тестируемой страницы
from pages.catalog_page import CatalogPage

# для маркировки тестов
import pytest


@pytest.mark.catalog_page
@pytest.mark.medium
@pytest.mark.basket
def test_all_goods_can_be_added_to_basket_from_meat_category_page(selenium):
    """Все товары с первой страницы категории "мясо, птица, колбаса" могут быть добавлены в корзину."""
    # для тестирования другой категории нужно просто сменить одну переменную meat_category

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = CatalogPage(selenium)
    selenium.get(page.url)
    # соглашение с cookie
    page.wait_scroll_and_click_on_element(page.cookie_agree_button)
    # клик на категорию "мясо, птица, колбаса"
    page.wait_scroll_and_click_on_element(page.meat_category)

    # добавление каждого элемента на странице в корзину (локатор исчезает после добавления, поэтому всегда 0 элемент)
    amount_of_elements = len(selenium.find_elements(*page.add_to_basket_button))
    count = int(amount_of_elements)
    while True:
        page.wait_scroll_and_click_on_one_of_elements(page.add_to_basket_button, 0)
        time.sleep(1)
        count -= 1
        if count == 0:
            break
    # ожидание, так число у корзины меняется не сразу
    time.sleep(1)

    # число у корзины должно совпадать с количеством добавленных товаров
    assert selenium.find_element(*page.amount_of_goods).text == str(
        amount_of_elements), "Не все товары добавлены в корзину"


@pytest.mark.catalog_page
@pytest.mark.medium
@pytest.mark.clickable
def test_all_categories_clickable(selenium):
    """Кликабельность всех категорий на странице каталога."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = CatalogPage(selenium)
    selenium.get(page.url)
    # соглашение с cookie
    page.wait_scroll_and_click_on_element(page.cookie_agree_button)

    # список локаторов категорий из каталога
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
    for i in range(len(category_list)):
        page.wait_scroll_and_click_on_element(category_list[i])
        url_after = selenium.current_url
        page.go_back()
        # без ожидания ломается сайт
        time.sleep(3)
        assert url_before != url_after, "Переход на другую страницу не осуществлен"
