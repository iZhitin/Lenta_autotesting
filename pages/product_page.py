# импортируем базовый класс для наследования всего основного функционала
from pages.base_page import BasePage
# для удобной работы с локаторами импортируем метод By
from selenium.webdriver.common.by import By


# класс страницы каталога
class ProductPage(BasePage):
    def __init__(self, driver, timeout=10):
        self.driver = driver
        # прибавляем к url главной страницы параметры пути ???
        page = BasePage(driver)
        self.url = page.url + 'product/yabloki-grenni-smit-ves-1kg-111129/'
        # ЕСЛИ не передать self.url в super(), то экземпляр.url будет гл. страницей из BasePage
        super().__init__(driver, self.url)

        # локаторы элементов страницы
        # фотография товара на странице товара
        self.image_in_product_page = (By.XPATH,
                                      '//*[@class="sku-page__image-container sku-images-slider__image-wrapper square image-zoom sku-images-slider__image-show-only image-zoom--hidden"]')

        # при наведении курсора на изображение для увеличения, его тег меняется - из класса уходит image-zoom--hidden
        self.image_magnifying = (By.XPATH,
                                 '//*[@class="sku-page__image-container sku-images-slider__image-wrapper square image-zoom sku-images-slider__image-show-only"]')
        # кнопка "добавить в корзину со страницы товара"
        self.add_to_basket_from_product_page_button = (By.CSS_SELECTOR, '.basket-sku-control.sku-page-control__basket-control')