# импортируем функционал применимый к любой странице
from pages.base_page import BasePage
# для удобной работы с локаторами импортируем метод By
from selenium.webdriver.common.by import By


# класс главной страницы
class MainPage(BasePage):
    def __init__(self, driver, url='', timeout=10):
        if url is False:
            self.url = "https://lenta.com/"
        super().__init__(driver, url, timeout)

        # локаторы элементов страницы

        # этот локатор не только в этом классе
        self.cookie_agree_button = (By.XPATH, '//*[text()="Согласен"]')

        # header
        self.go_to_catalog_from_ad = (By.XPATH,
                         '//*[@href="https://lenta.com/catalog/?utm_source=lweb&utm_medium=banner&utm_campaign=up"]')
        self.header_logo = (By.CSS_SELECTOR, '.header__logo')
        self.search_icon = (By.CSS_SELECTOR, '.icon.header__search-bar-icon') # продублирован ниже
        self.profile_icon = (By.XPATH, '//*[@href="/npl/authentication"]')
        self.liked_icon = (By.XPATH, '//*[@href="/shoppinglist/"]')
        self.cart_icon = (By.XPATH, '//*[@href="/order/cart/"]')

        # first banner
        # кнопки для пролистывания акций баннера
        self.right_buttons = (By.XPATH, '//*[@class="swiper-slider-button-next"]')
        self.left_buttons = (By.XPATH, '//*[@class="swiper-slider-button-prev"]')
        # одна из 5 акций баннера
        self.selection_board = (By.XPATH,
                          '//*[@src="https://lenta.servicecdn.ru/globalassets/slider-images/2022-06/1326x300__american-tourister_samsonite______.jpg"]')

        # элементы поиска
        # поиск во внешнем поле
        self.search_field = (By.CSS_SELECTOR, '.catalog-search__field')
        self.search_icon_button = (By.CSS_SELECTOR, '.catalog-search__icon')
        # поиск во внутреннем поле
        self.search_icon = (By.CSS_SELECTOR, '.icon.header__search-bar-icon')
        self.inner_search_field = (By.CSS_SELECTOR, '.catalog-search-popup__input')
        # результаты поиска
        self.search_results = (By.XPATH, '//*[text()="Результаты поиска"]')

    # авторизацию не получится использовать, так как нужны смс из телефона
