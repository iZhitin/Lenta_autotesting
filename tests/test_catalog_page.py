#!/usr/bin/python3
# -*- encoding=utf8 -*-

# первая строчка позволяет запускать код на разных OS, в случае если интерпретатор установлен в разных локациях
# вторая строка устанавливает кодировку

# для визуального контроля
import time
# для работы с cookie
import pickle

# импортируем класс тестируемой страницы
from pages.catalog_page import CatalogPage

# для запуска тестов через терминал:
# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests\test_catalog_page.py


def test_catalog_page(selenium):
    # создаем экземпляр класса тестируемой страницы
    page = CatalogPage(selenium)

    # page.url берется из самого первого класса
    page.get_url(page.url)


        # selenium.get('https://petfriends.skillfactory.ru/all_pets')
    time.sleep(3)
    # try:
    #     with open("my_cookies.txt", "rb") as cookiesfile:
    #         cookies = pickle.load(cookiesfile)
    #         for cookie in cookies:
    #             selenium.add_cookie(cookie)
    #     # selenium.get('https://petfriends.skillfactory.ru/all_pets')
    # except:
    #     pass

    # selenium.refresh()

    # a = selenium.find_elements(page.add_to_busket_button)
    # нумерация элементов - с нуля
    # selenium.find_element_by_xpath('//*[text()="Согласен"]').click()
    # элементы "в корзину" загораживаются верхней частью сайта (хэдером)
    page.scroll_wait_and_click_on_one_of_elements(page.add_to_busket_button, 2)
    time.sleep(3)
    selenium.refresh()




    time.sleep(3)
    assert False
    # клик на акционный блок
    # page.scroll_wait_and_click_on_element(page.selection)
    # клик на каталог из предложения в хэдере
    # page.scroll_wait_and_click_on_element(page.go_to_catalog_from_ad)
    # как работает переключение между окнами
    # selenium.switch_to.window(selenium.window_handles[0])
    # клик на категорию мясо, птица, колбаса
    # page.scroll_wait_and_click_on_element(page.meat_category)

#     with open("my_cookies.txt", "wb") as cookies:
# #         pickle.dump(selenium.get_cookies(), cookies)



