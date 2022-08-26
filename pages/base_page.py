# для парсинга параметров пути
import time
from urllib.parse import urlparse
# для явного ожидания
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# для выполнения действий
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
# для работы с json
import json
# для генерации id
import uuid
# для работы с cookie
import pickle

# для удобной работы с локаторами импортируем метод By
from selenium.webdriver.common.by import By


# класс основной страницы
class BasePage(object):
    """Класс, предоставляющий общий функционал, для работы со страницей. Но не с
    элементами страницы"""

    # конструктор класса - специальный метод с ключевым словом __init__ (по факту, конструктор __new__,
    # а это - инициализатор нового объекта класса)

    # при создании экземпляра класса в него передаются
    # объект веб-драйвера, адрес страницы и время ожидания элементов
    def __init__(self, driver, url='', timeout=10):
        self.driver = driver
        if not url:
            self.url = "https://lenta.com/"
        # добавим неявное ожидание ???
        self.driver.implicitly_wait(timeout)

    # функция выводит параметры пути URL, например: /search_results
    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    # сохранение скриншота
    def take_screenshot(self):
        # чтобы заработало, нужна предварительно созданная папка screenshots в корне проекта
        screenshot = 'screenshots/{0}.png'
        self.driver.save_screenshot(screenshot.format(str(uuid.uuid4().hex)))

    # прокрутка до элемента, ожидание видимости, движение мыши к центру элемента и клик
    def wait_scroll_and_click_on_element(self, locator):
        # локатор в формате (By.LOCATOR, 'locator')
        web_element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        # ПРОКРУТКА К ЭЛЕМЕНТУ В JS работает отлично, что не скажешь о прокрутке Selenium
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", web_element)
        # наведение мыши на центр элемента и клик
        ActionChains(self.driver).move_to_element(web_element).click(web_element).perform()

    # прокрутка до ОДНОГО ИЗ элементов, ожидание видимости, движение мыши к центру элемента и клик
    # нумерация с нуля
    def wait_scroll_and_click_on_one_of_elements(self, locator, index):
        # локатор в формате (By.LOCATOR, 'locator')
        # можно МЕНЯТЬ с any на all
        web_elements = WebDriverWait(self.driver, 20).until(EC.visibility_of_any_elements_located(locator))
        # ПРОКРУТКА К ЭЛЕМЕНТУ В JS работает отлично, что не скажешь о прокрутке Selenium
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", web_elements[index])
        # добавим нажатие кнопки "вверх" из-за того, что нужный элемент все время прячется
        # (выравнивание по верхней или нижней границе)
        ActionChains(self.driver)\
            .send_keys(Keys.ARROW_UP)\
            .send_keys(Keys.ARROW_UP)\
            .send_keys(Keys.ARROW_UP)\
            .move_to_element(web_elements[index])\
            .click(web_elements[index]).perform() # наведение мыши на центр элемента и клик
        # клик СРАБОТАЕТ, если передать в аргумент ЭЛЕМЕНТ !!!

    # ожидание видимости, движение мыши к центру элемента и клик
    def wait_and_click_on_one_of_elements(self, locator, index):
        # локатор в формате (By.LOCATOR, 'locator')
        # можно менять с any на all
        web_elements = WebDriverWait(self.driver, 20).until(EC.visibility_of_any_elements_located(locator))
        ActionChains(self.driver).move_to_element(web_elements[index]).click(web_elements[index]).perform()

    # возвращение на предыдущую страницу
    def go_back(self):
        # встроенный метод selenium .back() - назад ( .forward() - вперед) - не всегда стабилен
        try:
            self.driver.back()
        except:
            self.driver.execute_script("window.history.go(-1)")

    # задать масштаб страницы
    def zoom(self, value):
        # value - процент
        # после перезагрузки страницы масштаб возвращается к 100%
        self.driver.execute_script("document.body.style.zoom='{0}%'".format(value))

    # переключение на страницу по ее номеру
    def switch_tab(self, tab):
        # нумерация закладок с 0
        self.driver.switch_to.window(self.driver.window_handles[tab])

    # сохранение cookie
    def save_cookies(self):
        with open("my_cookies.txt", "wb") as cookies:
            pickle.dump(self.driver.get_cookies(), cookies)

    # чтение cookie
    def read_cookies(self):
        with open("my_cookies.txt", "rb") as cookiesfile:
            cookies = pickle.load(cookiesfile)
            for cookie in cookies:
                self.driver.add_cookie(cookie)

    # ??? надо проверять на реальном объекте
    # прокрутка снизу к верху, пока элемент не будет виден
    def scroll_from_down_to_up(self, locator):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        while True:
            ActionChains(self.driver).send_keys(Keys.UP).perform()
            time.sleep(0.2)
            if EC.visibility_of_any_elements_located(locator):
                break






# class ManyWebElements(WebElement):
#
#     def __getitem__(self, item):
#         """ Get list of elements and try to return required element. """
#
#         elements = self.find()
#         return elements[item]
#
#     def find(self, timeout=10):
#         """ Find elements on the page. """
#
#         elements = []
#
#         try:
#             elements = WebDriverWait(self._web_driver, timeout).until(
#                EC.presence_of_all_elements_located(self._locator)
#             )
#         except:
#             print(colored('Elements not found on the page!', 'red'))
#
#         return elements


    # для работы с невидимым элементом
    def wait_for_animation(self, selector):
        """
        Waits until jQuery animations have finished for the given jQuery  selector.
        """
        WebDriverWait(self.driver, 10).until(lambda driver: driver.execute_script(
            "return jQuery(%s).is(':animated')" % json.dumps(selector)) == False)

    def wait_for_ajax_loading(self, class_name):
        """
        Waits until the ajax loading indicator disappears.
        """
        WebDriverWait(self.driver, 10).until(lambda driver: len(driver.find_elements_by_class_name(
            class_name)) == 0)

    def wait_presence(self, locator):
        # локатор в формате (By.LOCATOR, 'locator')
        web_element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))
        web_element.click()
        return web_element