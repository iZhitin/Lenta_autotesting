# точка означает нахождение в одной директории
from .base_page import BasePage
# from .locators import AuthLocators

# для визуального контроля
import time


class AuthPage(BasePage):
    """Класс, наследующий общий функционал работы со страницей, инициализирует элементы страницы и
    методы работы с ними. Предназначен для страницы авторизации"""
    def __init__(self, driver, timeout=10):
        # наследуем функционал, передав параметры
        super().__init__(driver, timeout)
        # использование в ссылке слова login - плохая практика
        # открываем страницу
        url = "https://petfriends.skillfactory.ru/login"
        driver.get(url)
        # инициализируем элементы, найденные по локаторам
        self.email = driver.find_element(*AuthLocators.AUTH_EMAIL)
        self.password = driver.find_element(*AuthLocators.AUTH_PASSWORD)
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
        time.sleep(3)

    # функция вводит переданный email
    def enter_email(self, value):
        self.email.send_keys(value)

    # функция вводит переданный password
    def enter_password(self, value):
        self.password.send_keys(value)

    # функция нажимает на кнопку
    def click_btn(self):
        self.btn.click()

