#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from TestingPetFriendsSeleniumSPOM.pages.base import WebPage
from TestingPetFriendsSeleniumSPOM.pages.elements import WebElement
from TestingPetFriendsSeleniumSPOM.pages.elements import ManyWebElements


# элементы главной страницы яндекс маркета
# создаем класс с элементами страниц
class MainPage(WebPage):
    # есть возможность передать url
    def __init__(self, web_driver, url=''):
        if not url:
            # если нет, то проверка наличия параметра внешнего окружения или значение по умолчанию
            url = os.getenv("MAIN_URL") or 'https://market.yandex.ru/'
        # чтобы использовать родительский функционал, обратимся к классу родителя
        super().__init__(web_driver, url)

    # Main search field
    search = WebElement(id='header-search')

    # Search button
    search_run_button = WebElement(xpath='//button[@type="submit"]')

    # Titles of the products in search results
    products_titles = ManyWebElements(xpath='//a[contains(@href, "/product-") and @title!=""]')

    # Button to sort products by price
    sort_products_by_price = WebElement(css_selector='button[data-autotest-id="dprice"]')

    # Prices of the products in search results
    products_prices = ManyWebElements(xpath='//div[@data-zone-name="price"]//span/*[1]')
