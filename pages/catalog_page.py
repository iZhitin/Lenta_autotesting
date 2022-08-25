# импортируем функционал применимый к любой странице
from pages.base_page import BasePage
# для удобной работы с локаторами импортируем метод By
from selenium.webdriver.common.by import By


class CatalogPage(BasePage):
    def __init__(self, driver, timeout=10):
        self.driver = driver
        # прибавляем к url главной страницы параметры пути ?
        page = BasePage(driver)
        self.url = page.url + 'catalog/myaso-ptica-kolbasa/'
        # ЕСЛИ не передать self.url в super(), то будет открываться гл. страница из BasePage
        super().__init__(driver, self.url)

        # локаторы элементов страницы
        # self.add_to_busket_button = (By.CSS_SELECTOR, '.sku-card-small-basket-control__default-control')
        # self.add_to_busket_button = (By.XPATH, '//*[text()="В корзину"]')
        # self.add_to_busket_button = (By.CSS_SELECTOR, '.sku-card-small-basket-control.sku-card-small__control')
        self.add_to_busket_button = (By.CSS_SELECTOR, '.sku-card-small-basket-control__default-control')




