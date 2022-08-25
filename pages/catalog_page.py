# импортируем функционал применимый к любой странице
from pages.base_page import BasePage
# для удобной работы с локаторами импортируем метод By
from selenium.webdriver.common.by import By


# класс страницы каталога
class CatalogPage(BasePage):
    def __init__(self, driver, timeout=10):
        self.driver = driver
        # прибавляем к url главной страницы параметры пути ?
        page = BasePage(driver)
        self.url = page.url + 'catalog/'
        # ЕСЛИ не передать self.url в super(), то будет открываться гл. страница из BasePage
        super().__init__(driver, self.url)

        # локаторы элементов страницы
        self.meat_category = (By.CSS_SELECTOR, 'a[href="/catalog/myaso-ptica-kolbasa/"]')

        # локаторы элементов элементов страницы
        self.add_to_busket_button = (By.CSS_SELECTOR, '.sku-card-small-basket-control__default-control')
        # self.add_to_busket_button = (By.CSS_SELECTOR, '.sku-card-small-basket-control__default-control')
        # self.add_to_busket_button = (By.XPATH, '//*[text()="В корзину"]')
        # self.add_to_busket_button = (By.CSS_SELECTOR, '.sku-card-small-basket-control.sku-card-small__control')

        # этот локатор не только в этом классе
        self.cookie_agree_button = (By.XPATH, '//*[text()="Согласен"]')

        # количество (цифра у корзины) добавленных товаров
        self.amount_of_goods = (By.CSS_SELECTOR, ".header-catalog-link__counter.js-sku-counter-basket.header-catalog-link__counter--show")





