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
        self.go_to_catalog_from_ad = (By.XPATH,
                         '//*[@href="https://lenta.com/catalog/?utm_source=lweb&utm_medium=banner&utm_campaign=up"]')
        self.right_buttons = (By.XPATH, '//*[@class="swiper-slider-button-next"]')
        self.left_buttons = (By.XPATH, '//*[@class="swiper-slider-button-prev"]')
        self.selection_board = (By.XPATH,
                          '//*[@src="https://lenta.servicecdn.ru/globalassets/slider-images/2022-06/1326x300__american-tourister_samsonite______.jpg"]')
        # этот локатор не только в этом классе
        self.cookie_agree_button = (By.XPATH, '//*[text()="Согласен"]')

    # авторизацию не получится использовать, так как нужны смс из телефона


