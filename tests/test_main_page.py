#!/usr/bin/python3
# -*- encoding=utf8 -*-

# первая строчка позволяет запускать код на разных OS, в случае если интерпретатор установлен в разных локациях
# вторая строка устанавливает кодировку

# для визуального контроля (в некоторых случаях, для ожидания загрузки страницы)
import time

# импортируем класс тестируемой страницы и элементы из других классов страниц
from pages.main_page import MainPage
from pages.catalog_page import CatalogPage
from pages.product_page import ProductPage

# для маркировки и параметризации тестов
import pytest
from generate_functions import *
from parsed_products import product_list


@pytest.mark.main_page
@pytest.mark.fast
@pytest.mark.cookie
def test_not_to_ask_cookie_twice(selenium):
    """После соглашения с cookie и перезагрузки страницы, запроса на соглашение больше не появляется."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)
    # соглашение с cookie
    page.wait_scroll_and_click_on_element(page.cookie_agree_button)

    # перезагрузка и проверка наличия кнопки после нее
    selenium.refresh()
    flag = None
    try:
        selenium.find_element(*page.cookie_agree_button)
    except:
        flag = False
        # raise selenium.common.exceptions.NoSuchElementException

    assert flag is False, "После соглашения с cookie и" \
                          "перезагрузки, они запрашиваются" \
                          "снова"


@pytest.mark.main_page
@pytest.mark.fast
@pytest.mark.banner
def test_banner_buttons(selenium):
    """Проверка цикличности перелистывания акций в начальном баннере."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)
    # соглашение с cookie
    page.wait_scroll_and_click_on_element(page.cookie_agree_button)

    # прокликивание стрелки вправо на первом баннере
    page.wait_and_click_on_one_of_elements(page.right_buttons, 0)
    page.wait_and_click_on_one_of_elements(page.right_buttons, 0)
    page.wait_and_click_on_one_of_elements(page.right_buttons, 0)
    page.wait_and_click_on_one_of_elements(page.right_buttons, 0)
    # возвращения от последнего элемента к первому при помощи правой кнопкой
    page.wait_and_click_on_one_of_elements(page.right_buttons, 0)
    # наоборот: с первого на последний и с последнего на предпоследний
    page.wait_and_click_on_one_of_elements(page.left_buttons, 0)
    page.wait_and_click_on_one_of_elements(page.left_buttons, 0)


@pytest.mark.main_page
@pytest.mark.fast
@pytest.mark.banner
def test_hidden_promo_in_banner(selenium):
    """Ожидание появления акции в начальном баннере."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)
    # соглашение с cookie
    page.wait_scroll_and_click_on_element(page.cookie_agree_button)

    # клик на акционный акцию в начальном баннере
    page.wait_scroll_and_click_on_element(page.selection_board)
    # переключение на страницу с открывшейся акцией и скриншот этой страницы
    page.switch_tab(1)
    page.take_screenshot()


@pytest.mark.main_page
@pytest.mark.fast
@pytest.mark.banner
@pytest.mark.header
@pytest.mark.clickable
def test_banner_in_header_clickable(self, selenium):
    """Кликабельность баннера в хэдере."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)

    # клик на баннер и проверка перехода на другую страницу
    page.wait_scroll_and_click_on_element(page.go_to_catalog_from_ad)
    assert selenium.current_url == 'https://lenta.com/catalog/?utm_source=lweb&utm_medium=banner&utm_campaign=up', \
        "Открылась неожиданная страница или переход не осуществлен вовсе"


@pytest.mark.main_page
@pytest.mark.fast
@pytest.mark.header
@pytest.mark.clickable
def test_catalog_button_in_header_clickable(selenium):
    """Работоспособность кнопки каталога в хэдере."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)

    # установим размер окна (разрешение меняется тоже), чтобы нужный элемент появился на странице
    selenium.set_window_size(1035, 768)
    # клик на кнопку каталога
    page.wait_scroll_and_click_on_element(page.catalog)

    # проверка перехода на другую страницу
    assert selenium.current_url == 'https://lenta.com/catalog/', \
        "Открылась неожиданная страница или переход не осуществлен вовсе"


@pytest.mark.main_page
@pytest.mark.fast
@pytest.mark.header
@pytest.mark.clickable
def test_logo_icon_in_header_clickable(selenium):
    """Клик на лого в хэдере ведет на главную страницу."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)

    # проверка перехода на главную страницу
    page.wait_scroll_and_click_on_element(page.header_logo)
    assert selenium.current_url == 'https://lenta.com/', \
        "Переход на главную страницу не осуществляется"


@pytest.mark.main_page
@pytest.mark.fast
@pytest.mark.map
@pytest.mark.header
@pytest.mark.clickable
def test_store_button_in_header_clickable(selenium):
    """Клик на кнопку "магазины" в хэдере открывает страницу с яндекс-картой."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)

    page.wait_scroll_and_click_on_element(page.stores)
    time.sleep(1)
    assert page.is_presented(page.store_window) is True, \
        "Окно с картой не открывается"


@pytest.mark.main_page
@pytest.mark.fast
@pytest.mark.map
@pytest.mark.header
@pytest.mark.clickable
def test_delivery_button_in_header_clickable(selenium):
    """Открытие окна с яндекс-картами после клика на кнопку "доставка" в хэдере."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)

    # нажатие на кнопки "доставка" в хэдере
    page.wait_scroll_and_click_on_element(page.delivery)
    time.sleep(1)
    # нажатие на внутреннюю кнопку "Магазины / Самовывоз"
    page.wait_scroll_and_click_on_element(page.inner_store_button)

    assert page.is_presented(page.delivery_window) is True, \
        "Окно с картой не открывается"


@pytest.mark.main_page
@pytest.mark.fast
@pytest.mark.map
@pytest.mark.input
@pytest.mark.xfail
def test_input_invalid_store_address_works(selenium):
    """Поиск магазина по существующему адресу, введенному в свободном стиле."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)

    # нажатие на кнопки "магазины" в хэдере
    page.wait_scroll_and_click_on_element(page.stores)
    time.sleep(1)
    # нажатие на внутреннюю кнопку "Магазины / Самовывоз"
    page.wait_scroll_and_click_on_element(page.inner_store_button)

    # адрес магазина (или самовывоза)
    first = "Санкт-Петербург "
    second = "Обводного  "
    third = "канала "
    fourth = "118"
    text = first + second + third + fourth

    # клик на текстовое поле, очистка, ввод и отправка адреса
    page.wait_scroll_and_click_on_element(page.inner_address_input_field)
    page.clear_and_enter_text(page.inner_address_input_field, text)
    page.wait_scroll_and_click_on_element(page.inner_show_addresses_by_list_button)
    time.sleep(3)

    assert page.wait_to_be_clickable_of_one_of_elements(page.dropped_list_of_store_addresses, 0), \
        "Первый магазин из выпадающего списка - не кликабелен"


@pytest.mark.main_page
@pytest.mark.fast
@pytest.mark.map
@pytest.mark.input
@pytest.mark.clickable
def test_input_valid_store_address_works(selenium):
    """Поиск магазина по существующему адресу, введенному в строгом стиле."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)

    # нажатие на кнопки "магазины" в хэдере
    page.wait_scroll_and_click_on_element(page.stores)
    time.sleep(1)
    # нажатие на внутреннюю кнопку "Магазины / Самовывоз"
    page.wait_scroll_and_click_on_element(page.inner_store_button)

    # адрес магазина (или самовывоза)
    text = "ул. 1-я Красноармейская, д. 15, лит. А"
    # клик на текстовое поле, очистка, ввод и отправка адреса
    page.wait_scroll_and_click_on_element(page.inner_address_input_field)
    page.clear_and_enter_text(page.inner_address_input_field, text)
    page.wait_scroll_and_click_on_element(page.inner_show_addresses_by_list_button)
    time.sleep(3)

    assert page.wait_to_be_clickable_of_one_of_elements(page.dropped_list_of_store_addresses, 0), \
        "Первый магазин из выпадающего списка - не кликабелен"


@pytest.mark.main_page
@pytest.mark.fast
@pytest.mark.map
@pytest.mark.input
def test_choose_after_input_valid_store_address(selenium):
    """Переход к первому магазину из выпадающего списка и проверка его выбора."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)

    # нажатие на кнопки "магазины" в хэдере
    page.wait_scroll_and_click_on_element(page.stores)
    time.sleep(1)
    # нажатие на внутреннюю кнопку "Магазины / Самовывоз"
    page.wait_scroll_and_click_on_element(page.inner_store_button)

    # адрес магазина (или самовывоза)
    text = "ул. 1-я Красноармейская, д. 15, лит. А"
    # клик на текстовое поле, очистка, ввод и отправка адреса
    page.wait_scroll_and_click_on_element(page.inner_address_input_field)
    page.clear_and_enter_text(page.inner_address_input_field, text)
    page.wait_scroll_and_click_on_element(page.inner_show_addresses_by_list_button)
    time.sleep(5)

    # клик на первый элемент из выпадающего списка
    page.wait_scroll_and_click_on_one_of_elements(page.dropped_list_of_store_addresses, 0)
    time.sleep(3)
    page.wait_scroll_and_click_on_element(page.inner_choose_store_button)
    time.sleep(7)

    assert 'Красноармейская' in page.wait_scroll_and_get_text_from_element(page.address),\
        "Адрес в системе отличается от введенного"


@pytest.mark.main_page
@pytest.mark.fast
@pytest.mark.map
@pytest.mark.input
@pytest.mark.xfail
def test_input_delivery_address_works(selenium):
    """В системе сохраняется введенный пользователем адрес доставки."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)

    # нажатие на кнопки "доставка" в хэдере
    page.wait_scroll_and_click_on_element(page.delivery)
    time.sleep(1)
    # нажатие на внутреннюю кнопку "Магазины / Самовывоз"
    page.wait_scroll_and_click_on_element(page.inner_store_button)

    # адрес доставки
    first = "Санкт-петербург "
    second = "Дворцовая "
    third = "площадь "
    fourth = "2"
    text = first + second + third + fourth
    # клик на текстовое поле, очистка, ввод и отправка адреса
    page.wait_scroll_and_click_on_element(page.inner_address_input_field)
    page.clear_and_enter_text(page.inner_address_input_field, text)
    page.wait_scroll_and_click_on_element(page.address_confirmation_button)
    time.sleep(5)

    assert second in page.wait_scroll_and_get_text_from_element(page.address), \
        "Адрес в системе отличается от введенного"


@pytest.mark.main_page
@pytest.mark.fast
@pytest.mark.header
@pytest.mark.clickable
def test_search_icon_in_header_clickable(selenium):
    """Проверка кликабельности иконки поиска."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)

    page.wait_scroll_and_click_on_element(page.search_icon)


@pytest.mark.main_page
@pytest.mark.fast
@pytest.mark.header
@pytest.mark.clickable
def test_profile_icon_clickable_in_header_at_100_zoom(selenium):
    """Проверка кликабельности иконки поиска при масштабе 100%"""
    selenium.set_window_size(1035, 768)

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)

    page.wait_scroll_and_click_on_element(page.profile_icon)
    time.sleep(1)


@pytest.mark.main_page
@pytest.mark.fast
@pytest.mark.header
@pytest.mark.clickable
def test_profile_icon_in_header_clickable_at_110_zoom(selenium):
    """Проверка кликабельности иконки поиска при масштабе 110%"""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)

    page.wait_scroll_and_click_on_element(page.profile_icon)
    time.sleep(1)


@pytest.mark.main_page
@pytest.mark.fast
@pytest.mark.header
@pytest.mark.clickable
def test_liked_icon_in_header_clickable(selenium):
    """Проверка кликабельности иконки "избранное"."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)

    page.wait_scroll_and_click_on_element(page.liked_icon)
    time.sleep(1)


@pytest.mark.main_page
@pytest.mark.fast
@pytest.mark.header
@pytest.mark.clickable
def test_header_cart_icon_in_header_clickable(selenium):
    """Проверка кликабельности иконки "корзина" (тележка)."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)

    page.wait_scroll_and_click_on_element(page.cart_icon)
    time.sleep(1)


@pytest.mark.main_page
@pytest.mark.fast
@pytest.mark.header
@pytest.mark.input
def test_search_field(selenium):
    """Проверка поиска слова "капуста"."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)

    # установим размер окна (разрешение меняется тоже), чтобы нужный элемент был на странице
    selenium.set_window_size(1035, 768)

    # обращение к поисковому полю, ввод и нажатие кнопки поиск
    page.wait_scroll_and_click_on_element(page.search_field)
    page.clear_and_enter_text(page.search_field, 'капуста')
    page.wait_scroll_and_click_on_element(page.search_icon_button)

    assert page.is_presented(page.successful_search_results) is True, \
        "На странице нет элемента с фразой 'Результаты поиска'"


@pytest.mark.main_page
@pytest.mark.fast
@pytest.mark.footer
@pytest.mark.clickable
def test_privacy_policy_in_footer_clickable(selenium):
    """Проверка кликабельности кнопки "политика конфиденциальности"."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)
    # соглашение с cookie
    page.wait_scroll_and_click_on_element(page.cookie_agree_button)

    page.wait_scroll_and_click_on_element(page.privacy_policy)
    assert selenium.current_url == 'https://lenta.com/pokupatelyam/privacy-policy/', \
        "Переход на страницу с политикой конфиденциальности не осуществлен"


@pytest.mark.main_page
@pytest.mark.fast
@pytest.mark.footer
@pytest.mark.clickable
def test_phone_icon_in_footer_clickable(selenium):
    """Проверка кликабельности номера телефона."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)
    # соглашение с cookie
    page.wait_scroll_and_click_on_element(page.cookie_agree_button)

    # клик на элемент
    page.wait_scroll_and_click_on_element(page.phone_link)
    time.sleep(1)
    # уведомление на уровне браузера появляется, но selenium его не видит
    # selenium.switch_to_alert.accept()


@pytest.mark.main_page
@pytest.mark.fast
@pytest.mark.footer
@pytest.mark.clickable
def test_telegram_icon_link_in_footer_clickable(selenium):
    """Проверка кликабельности контакта в telegram."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)
    # соглашение с cookie
    page.wait_scroll_and_click_on_element(page.cookie_agree_button)

    # клик на элемент
    page.wait_scroll_and_click_on_element(page.telegram_icon_link)
    time.sleep(1)


@pytest.mark.main_page
@pytest.mark.fast
@pytest.mark.footer
@pytest.mark.clickable
def test_whatsapp_icon_link_in_footer_clickable(selenium):
    """Проверка кликабельности контакта в whatsapp."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)
    # соглашение с cookie
    page.wait_scroll_and_click_on_element(page.cookie_agree_button)

    # клик на элемент
    page.wait_scroll_and_click_on_element(page.whatsapp_icon_link)
    time.sleep(1)


@pytest.mark.main_page
@pytest.mark.fast
@pytest.mark.footer
@pytest.mark.clickable
def test_about_company_link_in_footer_clickable(selenium):
    """Проверка кликабельности ссылки "о компании"."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)
    # соглашение с cookie
    page.wait_scroll_and_click_on_element(page.cookie_agree_button)

    # клик на элемент
    page.wait_scroll_to_center_and_click_on_element(page.about_company)
    # если не прокручивать до того, пока элемент не будет в середине, то он
    # будет чем-то загражден и клик придется на другой элемент
    assert selenium.current_url == 'https://lenta.com/o-kompanii/', \
        "Переход на страницу 'о компании' не осуществлен"


@pytest.mark.main_page
@pytest.mark.fast
@pytest.mark.footer
@pytest.mark.clickable
def test_to_customers_link_in_footer_clickable(selenium):
    """Проверка кликабельности ссылки "о компании"."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)
    # соглашение с cookie
    page.wait_scroll_and_click_on_element(page.cookie_agree_button)

    # клик на элемент
    page.wait_scroll_to_center_and_click_on_element(page.to_customers)
    assert selenium.current_url == 'https://lenta.com/pokupatelyam/', \
        "Переход на страницу 'покупателям' не осуществлен"


@pytest.mark.main_page
@pytest.mark.fast
@pytest.mark.footer
@pytest.mark.clickable
def test_to_legal_persons_link_in_footer_clickable(selenium):
    """Проверка кликабельности ссылки "юридическим лицам"."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)
    # соглашение с cookie
    page.wait_scroll_and_click_on_element(page.cookie_agree_button)

    # клик на элемент
    page.wait_scroll_to_center_and_click_on_element(page.to_legal_persons)
    assert selenium.current_url == 'https://lenta.com/postavshchikam/', \
        "Переход на страницу 'поставщикам' не осуществлен"


@pytest.mark.main_page
@pytest.mark.medium
@pytest.mark.footer
@pytest.mark.clickable
def test_links_in_footer_clickable(selenium):
    """Проверка кликабельности блока ссылок в футере."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)
    # соглашение с cookie
    page.wait_scroll_and_click_on_element(page.cookie_agree_button)

    # прокликивание элементов
    for i in range(len(selenium.find_elements(*page.footer_links))):
        page.wait_scroll_and_click_on_one_of_elements(page.footer_links, i)
        # так как некоторые ссылки открывают новую страницу:
        page.switch_tab(0)
        time.sleep(1.5)


@pytest.mark.main_page
@pytest.mark.fast
@pytest.mark.footer
@pytest.mark.clickable
def test_estimate_website_link_in_footer_clickable(selenium):
    """Проверка кликабельности ссылки "оценить работу сайта" в футере."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)
    # соглашение с cookie
    page.wait_scroll_and_click_on_element(page.cookie_agree_button)

    # клик на элемент
    page.wait_scroll_and_click_on_element(page.estimate_website)
    assert page.is_presented(page.feedback_form) is True, \
        "Фидбэк форма не всплыла"


@pytest.mark.main_page
@pytest.mark.fast
@pytest.mark.footer
@pytest.mark.clickable
def test_mobile_app_icon_links_in_footer_clickable(selenium):
    """Проверка кликабельности ссылок на мобильные приложения в футере."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)
    # соглашение с cookie
    page.wait_scroll_and_click_on_element(page.cookie_agree_button)

    # прокликивание иконок (ссылок) на приложения
    for i in range(len(selenium.find_elements(*page.mobile_applications))):
        page.wait_and_click_on_one_of_elements(page.mobile_applications, i)
        # можно возвращаться на вкладку
        # page.switch_tab(0)
    time.sleep(3)


@pytest.mark.main_page
@pytest.mark.fast
@pytest.mark.footer
@pytest.mark.clickable
def test_social_media_icon_links_in_footer_clickable(selenium):
    """Проверка кликабельности ссылок на социальные сети в футере."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)
    # соглашение с cookie
    page.wait_scroll_and_click_on_element(page.cookie_agree_button)

    # прокликивание иконок (ссылок) на соцсети
    for i in range(len(selenium.find_elements(*page.social_medias))):
        page.wait_and_click_on_one_of_elements(page.social_medias, i)
        # можно возвращаться на вкладку
        # page.switch_tab(0)
    time.sleep(3)


@pytest.mark.main_page
@pytest.mark.medium
@pytest.mark.xfail
@pytest.mark.basket
def test_all_goods_can_be_added_to_basket_from_main_page(selenium):
    """Все видимые товары с главной страницы могут быть добавлены в корзину."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)
    # соглашение с cookie
    page.wait_scroll_and_click_on_element(page.cookie_agree_button)

    # добавление каждого элемента на странице в корзину (локатор исчезает после добавления, поэтому всегда 0 элемент)
    amount_of_elements = len(selenium.find_elements(*page.add_to_basket_button))
    count = int(amount_of_elements)
    while True:
        try:
            page.wait_scroll_and_click_on_one_of_elements(page.add_to_basket_button, 0)
            time.sleep(1)
            count -= 1
            if count == 0:
                break
        except:
            break
    # ожидание, так число у корзины меняется не сразу
    time.sleep(1)

    # число у корзины должно совпадать с количеством добавленных товаров
    assert selenium.find_element(*page.amount_of_goods).text == str(
        amount_of_elements), "Не все товары добавлены в корзину"


# не рабочий тест
# @pytest.mark.main_page
# @pytest.mark.medium
# @pytest.mark.xfail
# @pytest.mark.basket
# def test_all_hidden_goods_can_be_added_to_basket_from_main_page(selenium):
#     """Все скрытые товары с главной страницы могут быть добавлены в корзину."""
#
#     # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
#     page = MainPage(selenium)
#     selenium.get(page.url)
#     # соглашение с cookie
#     page.wait_scroll_and_click_on_element(page.cookie_agree_button)
#
#     # добавление каждого элемента на странице в корзину (локатор исчезает после добавления, поэтому всегда 0 элемент)
#     i = 10
#     while True:
#         while True:
#             try:
#                 page.wait_scroll_and_click_on_one_of_elements(page.add_to_basket_button, 0)
#             except:
#                 page.wait_scroll_and_click_on_one_of_elements(page.right_buttons, i)
#         i -= 1
#         if i < 0:
#             break


@pytest.mark.main_page
@pytest.mark.long
@pytest.mark.input
@pytest.mark.parametrize("search_text",
                             product_list,
                             ids=product_list)
def test_positive_search_requests(selenium, search_text):
    """Поиск наличия 1647 продуктов на сайте."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)

    # установим размер окна (разрешение меняется тоже), чтобы нужный элемент был на странице
    selenium.set_window_size(1035, 768)

    # обращение к поисковому полю, ввод и нажатие кнопки поиск
    page.wait_scroll_and_click_on_element(page.search_field)
    page.clear_and_enter_text(page.search_field, search_text)
    page.wait_scroll_and_click_on_element(page.search_icon_button)
    # 1.5 секунды ожидания - неудачный поиск все-равно долго ждет
    assert page.is_presented(page.successful_search_results, 1.5) is True, \
        "На странице нет элемента с фразой 'Результаты поиска'"


@pytest.mark.main_page
@pytest.mark.medium
@pytest.mark.input
@pytest.mark.parametrize("search_text",
                             [russian_chars(), russian_chars().upper(),
                              english_chars(), english_chars().upper(),
                              digits(3), generate_string(100), special_chars(),
                              chinese_chars(), chinese_chars().upper(), empty_space(30), everything(3)],
                             ids=['russian_chars', 'RUSSIAN_CHARS', 'english_chars', 'ENGLISH_CHARS',
                                  'digits', '1100 symbols', 'special_chars', 'chinese_chars', 'CHINESE_CHARS',
                                  '30_spaces', 'combination_of_previous'])
def test_negative_search_requests(selenium, search_text):
    """Негативное тестирование поискового поля."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)

    # установим размер окна (разрешение меняется тоже), чтобы нужный элемент был на странице
    selenium.set_window_size(1035, 768)

    # обращение к поисковому полю, ввод и нажатие кнопки поиск
    page.wait_scroll_and_click_on_element(page.search_field)
    page.clear_and_enter_text(page.search_field, search_text)
    page.wait_scroll_and_click_on_element(page.search_icon_button)

    assert page.is_presented(page.unsuccessful_search_results) is True, \
        "На странице нет элемента с фразой 'Мы ничего не нашли'"


@pytest.mark.main_page
@pytest.mark.medium
@pytest.mark.user
@pytest.mark.basket
def test_user_story_pickup(selenium):
    """Имитация действий пользователя: выбор места самовывоза и добавление товаров
    (2 - из категорий в каталоге, 2 - из карточек товаров, 3 - из поиска)."""

    # создаем экземпляр класса тестируемой страницы и открываем url, указанный в классе
    page = MainPage(selenium)
    selenium.get(page.url)
    # соглашение с cookie
    page.wait_scroll_and_click_on_element(page.cookie_agree_button)

    # нажатие на кнопку "магазины" в хэдере
    page.wait_scroll_and_click_on_element(page.stores)
    time.sleep(3)
    # нажатие на внутреннюю кнопку "Магазины / Самовывоз"
    page.wait_scroll_and_click_on_element(page.inner_store_button)

    # адрес магазина (или самовывоза)
    text = "наб. Обводного канала, д. 118, к. 7, лит. А"
    # клик на текстовое поле, очистка, ввод и отправка адреса
    page.wait_scroll_and_click_on_element(page.inner_address_input_field)
    page.clear_and_enter_text(page.inner_address_input_field, text)
    page.wait_scroll_and_click_on_element(page.inner_show_addresses_by_list_button)
    time.sleep(5)

    # выбор первого магазина из выпадающего списка и подтверждение
    page.wait_scroll_and_click_on_one_of_elements(page.dropped_list_of_store_addresses, 0)
    page.wait_scroll_and_click_on_element(page.inner_choose_store_button)
    # ожидание, так как страница долго загружается
    time.sleep(10)

    # чтобы кнопка каталога и поисковое поле стали доступны:
    selenium.set_window_size(1035, 768)

    # добавление товаров в корзину из категорий
    catalog = CatalogPage(selenium)
    page.wait_scroll_and_click_on_element(page.catalog)
    page.wait_scroll_and_click_on_element(catalog.meat_category)
    page.wait_scroll_and_click_on_one_of_elements(page.add_to_basket_button, 0)
    page.wait_scroll_and_click_on_element(page.catalog)
    page.wait_scroll_and_click_on_element(catalog.fruits_and_veg_category)
    page.wait_scroll_and_click_on_one_of_elements(page.add_to_basket_button, 1)

    # добавление товаров в корзину из карточек
    product = ProductPage(selenium)
    page.wait_scroll_and_click_on_element(page.catalog)
    page.wait_scroll_and_click_on_element(catalog.for_pets_category)
    page.wait_scroll_and_click_on_one_of_elements(page.product_card, 0)
    page.wait_scroll_to_center_and_click_on_element(product.add_to_basket_from_product_page_button)
    page.wait_scroll_and_click_on_element(page.catalog)
    page.wait_scroll_and_click_on_element(catalog.for_home_category)
    page.wait_scroll_and_click_on_one_of_elements(page.product_card, 3)
    page.wait_scroll_to_center_and_click_on_element(product.add_to_basket_from_product_page_button)

    # обращение к поисковому полю, ввод, нажатие кнопки поиск добавление товаров в корзину из результатов
    for product in ['орехи', 'ананас', 'яйца']:
        page.wait_scroll_and_click_on_element(page.search_field)
        page.clear_and_enter_text(page.search_field, product)
        page.wait_scroll_and_click_on_element(page.search_icon_button)
        page.wait_scroll_and_click_on_one_of_elements(page.add_to_basket_button, 3)
        # ожидание, так как товары добавляются не сразу
        time.sleep(3)

    # проверка соответствия количества позиций в корзине добавленным позициям
    page.wait_scroll_and_click_on_element(page.cart_icon)
    time.sleep(3)
    assert len(selenium.find_elements(*page.content_of_basket)) == 7, \
        "Количество добавленных позиций не соответствует количеству позиций в корзине"
