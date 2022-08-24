# для парсинга параметров пути
from urllib.parse import urlparse
# для явного ожидания
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# для выполнения действий
from selenium.webdriver.common.action_chains import ActionChains
# для удобной работы с локаторами импортируем метод By
from selenium.webdriver.common.by import By
# для работы с json
import json
# для генерации id
import uuid


class BasePage(object):
    """Класс, предоставляющий общий функционал, для работы со страницей. Но не с
    элементами страницы"""

    # конструктор класса - специальный метод с ключевым словом __init__ (по факту, конструктор __new__,
    # а это - инициализатор нового объекта класса)

    # при создании экземпляра класса в него передаются
    # объект веб-драйвера, адрес страницы и время ожидания элементов
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        # добавим неявное ожидание
        self.driver.implicitly_wait(timeout)

    # функция выводит параметры пути URL, например: /search_results
    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

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

    # сохранение скриншота
    def take_screenshot(self):
        # чтобы заработало, нужна предварительно созданная папка screenshots
        screenshot = 'screenshots/{0}.png'
        self.driver.save_screenshot(screenshot.format(str(uuid.uuid4().hex)))

    # прокрутка до элемента, ожидание видимости, движение мыши к центру элемента и клик
    def scroll_wait_and_click_on_element(self, locator):
        # локатор в формате (By.LOCATOR, 'locator')
        web_element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        # ПРОКРУТКА К ЭЛЕМЕНТУ В JS работает отлично, что не скажешь о прокрутке Selenium
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", web_element)
        # наведение мыши на центр элемента и клик
        ActionChains(self.driver).move_to_element(web_element).click().perform()


