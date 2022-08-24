# импортируем функционал применимый к любой странице
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver, url='', timeout=10):
        if url is False:
            url = "https://lenta.com/"
        # super().__init__(self, driver, timeout, url)
        super().__init__(driver, url, timeout)

    def get_url(self, url):
        self.driver.get(url)