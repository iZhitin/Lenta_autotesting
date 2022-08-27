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

    def ttest_header_catalog_button_clickable(self, selenium):
        # создаем экземпляр класса тестируемой страницы
        page = MainPage(selenium)
        # открываем главную страницу
        selenium.get(page.url)
        before = selenium.current_url
        # соглашение с cookie
        page.wait_scroll_and_click_on_element(page.cookie_agree_button)

        # установим размер окна (разрешение меняется тоже), чтобы нужный элемент был на странице
        # после изменения размера, нужный элемент подтягивается
        selenium.set_window_size(1035, 768)
        # клик на кнопку каталога
        page.wait_scroll_and_click_on_element(page.catalog)

        # проверка перехода на другую страницу
        after = selenium.current_url

        assert before != after \
               and after == 'https://lenta.com/catalog/', \
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

    def ttest_header_store_button_clickable(self, selenium):
        # создаем экземпляр класса тестируемой страницы
        page = MainPage(selenium)
        # открываем главную страницу
        selenium.get(page.url)
        # нажатие на кнопку "магазины" в хэдере
        page.wait_scroll_and_click_on_element(page.stores)
        time.sleep(3)
        assert page.is_presented(page.store_window) is True, \
            "Окно с картой не открывается"

    def ttest_header_delivery_button_clickable(self, selenium):
        # создаем экземпляр класса тестируемой страницы
        page = MainPage(selenium)
        # открываем главную страницу
        selenium.get(page.url)
        # нажатие на кнопку "магазины" в хэдере
        page.wait_scroll_and_click_on_element(page.delivery)
        time.sleep(3)
        assert page.is_presented(page.delivery_window) is True, \
            "Окно с картой не открывается"

    def ttest_header_search_icon_clickable(self, selenium):
        # создаем экземпляр класса тестируемой страницы
        page = MainPage(selenium)
        # открываем главную страницу
        selenium.get(page.url)
        page.wait_scroll_and_click_on_element(page.search_icon)

    def ttest_header_profile_icon_clickable_at_100_zoom(self, selenium):
        # создаем экземпляр класса тестируемой страницы
        page = MainPage(selenium)
        # открываем главную страницу
        selenium.get(page.url)
        selenium.set_window_size(1035, 768)
        page.wait_scroll_and_click_on_element(page.profile_icon)
        time.sleep(3)

    def ttest_header_profile_icon_clickable_at_110_zoom(self, selenium):
        # создаем экземпляр класса тестируемой страницы
        page = MainPage(selenium)
        # открываем главную страницу
        selenium.get(page.url)
        page.wait_scroll_and_click_on_element(page.profile_icon)
        time.sleep(3)

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

    def ttest_search_field(self, selenium):
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

    # @pytest.mark.footer
    def ttest_footer_privacy_policy_clickable(self, selenium):
        # создаем экземпляр класса тестируемой страницы
        page = MainPage(selenium)
        # открываем главную страницу
        selenium.get(page.url)
        # соглашение с cookie
        page.wait_scroll_and_click_on_element(page.cookie_agree_button)

        # клик на элемент
        page.wait_scroll_and_click_on_element(page.privacy_policy)

        assert selenium.current_url == 'https://lenta.com/pokupatelyam/privacy-policy/', \
            "Переход на страницу с политикой конфиденциальности не осуществлен"

    def ttest_footer_phone_icon_clickable(self, selenium):
        # создаем экземпляр класса тестируемой страницы
        page = MainPage(selenium)
        # открываем главную страницу
        selenium.get(page.url)
        # соглашение с cookie
        page.wait_scroll_and_click_on_element(page.cookie_agree_button)

        # клик на элемент
        page.wait_scroll_and_click_on_element(page.phone_link)
        time.sleep(3)
        # уведомление на уровне браузера появляется, но selenium его не видит
        # selenium.switch_to_alert.accept()
        time.sleep(3)

    def ttest_footer_telegram_icon_link_clickable(self, selenium):
        # создаем экземпляр класса тестируемой страницы
        page = MainPage(selenium)
        # открываем главную страницу
        selenium.get(page.url)
        # соглашение с cookie
        page.wait_scroll_and_click_on_element(page.cookie_agree_button)

        # клик на элемент
        page.wait_scroll_and_click_on_element(page.telegram_icon_link)
        time.sleep(3)

    def ttest_footer_whatsapp_icon_link_clickable(self, selenium):
        # создаем экземпляр класса тестируемой страницы
        page = MainPage(selenium)
        # открываем главную страницу
        selenium.get(page.url)
        # соглашение с cookie
        page.wait_scroll_and_click_on_element(page.cookie_agree_button)

        # клик на элемент
        page.wait_scroll_and_click_on_element(page.whatsapp_icon_link)
        time.sleep(3)

    def ttest_footer_about_company_link_clickable(self, selenium):
        # создаем экземпляр класса тестируемой страницы
        page = MainPage(selenium)
        # открываем главную страницу
        selenium.get(page.url)
        # соглашение с cookie
        page.wait_scroll_and_click_on_element(page.cookie_agree_button)

        # клик на элемент
        page.wait_scroll_to_center_and_click_on_element(page.about_company)
        # если не прокручивать до того, пока элемент не будет в середине, то он
        # будет чем-то загражден и клик придется на другой элемент
        time.sleep(3)
        assert selenium.current_url == 'https://lenta.com/o-kompanii/', \
            "Переход на страницу 'о компании' не осуществлен"

    def ttest_footer_to_customers_link_clickable(self, selenium):
        # создаем экземпляр класса тестируемой страницы
        page = MainPage(selenium)
        # открываем главную страницу
        selenium.get(page.url)
        # соглашение с cookie
        page.wait_scroll_and_click_on_element(page.cookie_agree_button)

        # клик на элемент
        page.wait_scroll_to_center_and_click_on_element(page.to_customers)
        time.sleep(3)
        assert selenium.current_url == 'https://lenta.com/pokupatelyam/', \
            "Переход на страницу 'покупателям' не осуществлен"

    def ttest_footer_to_legal_persons_link_clickable(self, selenium):
        # создаем экземпляр класса тестируемой страницы
        page = MainPage(selenium)
        # открываем главную страницу
        selenium.get(page.url)
        # соглашение с cookie
        page.wait_scroll_and_click_on_element(page.cookie_agree_button)

        # клик на элемент
        page.wait_scroll_to_center_and_click_on_element(page.to_legal_persons)
        time.sleep(3)
        assert selenium.current_url == 'https://lenta.com/postavshchikam/', \
            "Переход на страницу 'поставщикам' не осуществлен"

    def ttest_footer_links_clickable(self, selenium):
        # создаем экземпляр класса тестируемой страницы
        page = MainPage(selenium)
        # открываем главную страницу
        selenium.get(page.url)
        # соглашение с cookie
        page.wait_scroll_and_click_on_element(page.cookie_agree_button)

        # прокликивание элементов
        for i in range(len(selenium.find_elements(*page.footer_links))):
            page.wait_scroll_and_click_on_one_of_elements(page.footer_links, i)
            # так как некоторые ссылки открывают новую страницу:
            page.switch_tab(0)
            time.sleep(1.5)

    def ttest_footer_estimate_website_link_clickable(self, selenium):
        # создаем экземпляр класса тестируемой страницы
        page = MainPage(selenium)
        # открываем главную страницу
        selenium.get(page.url)
        # соглашение с cookie
        page.wait_scroll_and_click_on_element(page.cookie_agree_button)

        # клик на элемент
        page.wait_scroll_and_click_on_element(page.estimate_website)
        time.sleep(3)
        assert page.is_presented(page.feedback_form) is True, \
            "Фидбэк форма не всплыла"

    def ttest_footer_mobile_app_icon_links_clickable(self, selenium):
        # создаем экземпляр класса тестируемой страницы
        page = MainPage(selenium)
        # открываем главную страницу
        selenium.get(page.url)
        # соглашение с cookie
        page.wait_scroll_and_click_on_element(page.cookie_agree_button)

        # прокликивание иконок (ссылок) на приложения
        for i in range(len(selenium.find_elements(*page.mobile_applications))):
            page.wait_and_click_on_one_of_elements(page.mobile_applications, i)
            # можно возвращаться на вкладку
            # page.switch_tab(0)
        time.sleep(3)

    def ttest_footer_social_media_icon_links_clickable(self, selenium):
        # создаем экземпляр класса тестируемой страницы
        page = MainPage(selenium)
        # открываем главную страницу
        selenium.get(page.url)
        # соглашение с cookie
        page.wait_scroll_and_click_on_element(page.cookie_agree_button)

        # прокликивание иконок (ссылок) на соцсети
        for i in range(len(selenium.find_elements(*page.social_medias))):
            page.wait_and_click_on_one_of_elements(page.social_medias, i)
            # можно возвращаться на вкладку
            # page.switch_tab(0)
        time.sleep(3)
