# для работы с cookie
import pickle
# для неявного ожидания
import time
# для генерации id
import uuid
# для работы с url
from urllib.parse import urlparse

# для выполнения действий и явного ожидания
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    """Класс, содержащий в себе весь функционал фреймворка по работе со страницами и их элементами."""

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

    # сохранение скриншота
    def take_screenshot(self):
        # чтобы заработало, нужна предварительно созданная папка screenshots в корне проекта
        screenshot = 'screenshots/{0}.png'
        self.driver.save_screenshot(screenshot.format(str(uuid.uuid4().hex)))

    # прокрутка в самый низ, чтобы прогрузить страницу
    def scroll_to_page_bottom(self):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    # задать масштаб страницы
    def zoom(self, value):
        # value - процент
        # после перезагрузки страницы масштаб возвращается к 100%
        self.driver.execute_script("document.body.style.zoom='{0}%'".format(value))

    # возвращение на предыдущую страницу
    def go_back(self):
        # встроенный метод selenium .back() - назад ( .forward() - вперед) - не всегда стабилен
        # поменять местами
        try:
            self.driver.execute_script("window.history.go(-1)")
        except:
            self.driver.back()

    # поиск элемента на странице
    def seek_element(self, locator, timeout=10):
        element = None
        try:
            element = WebDriverWait(self.driver, timeout).until(
               EC.presence_of_element_located(locator))
        except:
            pass
            # print(colored('Element not found on the page!', 'red'))
            # print('Element is not found on the page!')
        # если элемент удается найти, то он возвращается (веб элемент)
        return element

    # проверка существования элемента на странице (True или False)
    def is_presented(self, locator, timeout=5):
        element = self.seek_element(locator, timeout)
        # немного не поддается пониманию, но работает
        return element is not None

    # реальное (а не видимое) переключение на страницу по ее номеру
    def switch_tab(self, tab):
        # нумерация закладок с 0
        self.driver.switch_to.window(self.driver.window_handles[tab])

    # прокрутка снизу к верху, пока элемент не будет виден ???
    def scroll_from_down_to_up_until_visibility_of_element(self, locator):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        while True:
            ActionChains(self.driver).send_keys(Keys.UP).perform()
            time.sleep(0.2)
            if EC.visibility_of_any_elements_located(locator):
                break

    # очистка и ввод текста в текстовое поле
    def clear_and_enter_text(self, locator, text, timeout=20):
        # локатор в формате (By.LOCATOR, 'locator')
        web_element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        # ПРОКРУТКА К ЭЛЕМЕНТУ В JS работает отлично, что не скажешь о прокрутке Selenium
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", web_element)
        ActionChains(self.driver).move_to_element(web_element).double_click()\
            .click_and_hold()\
            .send_keys(Keys.CLEAR)\
            .send_keys(text).perform()

    # очистка, ввод текста в текстовое поле и нажатие кнопки enter
    def clear_enter_text_and_press_return(self, locator, text, timeout=20):
        # локатор в формате (By.LOCATOR, 'locator')
        web_element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        # ПРОКРУТКА К ЭЛЕМЕНТУ В JS работает отлично, что не скажешь о прокрутке Selenium
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", web_element)
        ActionChains(self.driver).move_to_element(web_element).double_click()\
            .click_and_hold()\
            .send_keys(Keys.CLEAR)\
            .send_keys(text)\
            .send_keys(Keys.ENTER).perform()

                # для имитации ввода ни одна из следующих команд - не работает
        # в поисковом поле (внешнем и внутреннем) на сайте Лента
        # web_element.submit()
        # .send_keys(text\n)
        # .send_keys(u'\ue007')
        # .send_keys('\ue007')
        # .send_keys(Keys.ENTER)
        # .send_keys(Keys.RETURN)
        #
        # для изменения разрешения дисплея
        # from pyvirtualdisplay import Display
        # display = Display(size=(800, 600))
        # display.start()
        #
        # для нажатия клавиш
        # from pynput.keyboard import Key, Controller
        # keyboard = Controller()
        # keyboard.press(Key.enter)
        # keyboard.release(Key.enter)

    # нерабочая функция полной загрузки сайта
    # def wait_page_fully_loaded(self):
    #     # html_before = self.driver.page_source
    #     # WebDriverWait(self.driver, 10).until
    #     WebDriverWait(self.driver, 60).until(self.driver.execute_script("return document.readyState == 'complete';"))

    # ожидание видимости элемента, прокрутка и движение мыши к его центру
    def wait_and_scroll_to_element(self, locator, timeout=20):
        # локатор в формате (By.LOCATOR, 'locator')
        web_element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        # ПРОКРУТКА К ЭЛЕМЕНТУ В JS работает отлично, что не скажешь о прокрутке Selenium
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", web_element)
        # наведение мыши на центр элемента
        ActionChains(self.driver).move_to_element(web_element).perform()

    # ожидание видимости элемента, прокрутка, движение мыши к его центру и клик
    def wait_scroll_and_click_on_element(self, locator, timeout=20):
        # локатор в формате (By.LOCATOR, 'locator')
        web_element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        # ПРОКРУТКА К ЭЛЕМЕНТУ В JS работает отлично, что не скажешь о прокрутке Selenium
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", web_element)
        # наведение мыши на центр элемента и клик
        ActionChains(self.driver).move_to_element(web_element).click(web_element).perform()

    # ожидание видимости элемента, прокрутка до него в середине экрана, движение мыши к его центру и клик
    def wait_scroll_to_center_and_click_on_element(self, locator, timeout=20):
        # локатор в формате (By.LOCATOR, 'locator')
        web_element = WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))
        # ПРОКРУТКА К ЭЛЕМЕНТУ В JS работает отлично, что не скажешь о прокрутке Selenium
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", web_element)
        # наведение мыши на центр элемента и клик
        # нужно нажать вверх, так как после js-скрипта элемент еще не виден, чтобы продвинуть элемент к центру экрана
        ActionChains(self.driver)\
            .send_keys(Keys.ARROW_UP)\
            .send_keys(Keys.ARROW_UP)\
            .send_keys(Keys.ARROW_UP)\
            .send_keys(Keys.ARROW_UP)\
            .send_keys(Keys.ARROW_UP)\
            .move_to_element(web_element).click(web_element).perform()

    # ожидание видимости элемента, прокрутка до него и получение текста из его тега
    def wait_scroll_and_get_text_from_element(self, locator, timeout=20):
        # локатор в формате (By.LOCATOR, 'locator')
        web_element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        # ПРОКРУТКА К ЭЛЕМЕНТУ В JS работает отлично, что не скажешь о прокрутке Selenium
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", web_element)
        # возвращение внутреннего текста веб элемента
        return web_element.text

    # ожидание видимости, движение мыши к центру ОДНОГО ИЗ элементов и клик
    def wait_and_click_on_one_of_elements(self, locator, index, timeout=20):
        # локатор в формате (By.LOCATOR, 'locator')
        # можно МЕНЯТЬ с any на all
        web_elements = WebDriverWait(self.driver, timeout).until(EC.visibility_of_any_elements_located(locator))
        ActionChains(self.driver).move_to_element(web_elements[index]).click(web_elements[index]).perform()

    # ожидание видимости, прокрутка до ОДНОГО ИЗ элементов, движение мыши к центру и клик
    def wait_scroll_and_click_on_one_of_elements(self, locator, index, timeout=20):
        # локатор в формате (By.LOCATOR, 'locator')
        # можно МЕНЯТЬ с any на all
        web_elements = WebDriverWait(self.driver, timeout).until(EC.visibility_of_any_elements_located(locator))
        # ПРОКРУТКА К ЭЛЕМЕНТУ В JS работает отлично, что не скажешь о прокрутке Selenium
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", web_elements[index])
        # добавим нажатие кнопки "вверх" из-за того, что нужный элемент все время прячется
        # (выравнивание по верхней или нижней границе)
        ActionChains(self.driver)\
            .send_keys(Keys.ARROW_UP)\
            .send_keys(Keys.ARROW_UP)\
            .send_keys(Keys.ARROW_UP)\
            .move_to_element(web_elements[index])\
            .click(web_elements[index]).perform()
        # клик СРАБОТАЕТ, если передать в аргумент ЭЛЕМЕНТ !!!

    # проверка кликабельности ОДНОГО ИЗ элементов ???
    def wait_to_be_clickable_of_one_of_elements(self, locator, index, timeout=10):
        # локатор в формате (By.LOCATOR, 'locator')
        # можно МЕНЯТЬ с any на all
        try:
            web_elements = WebDriverWait(self.driver, timeout).until(EC.visibility_of_any_elements_located(locator))
            web_elements[index].click()
            return True
        except:
            return False

    # не использующиеся функции
            # для работы с невидимым элементом
    # def wait_for_animation(self, selector):
    #     """
    #     Waits until jQuery animations have finished for the given jQuery  selector.
    #     """
    #     WebDriverWait(self.driver, 10).until(lambda driver: driver.execute_script(
    #         "return jQuery(%s).is(':animated')" % json.dumps(selector)) == False)
    #
    # def wait_for_ajax_loading(self, class_name):
    #     """
    #     Waits until the ajax loading indicator disappears.
    #     """
    #     WebDriverWait(self.driver, 10).until(lambda driver: len(driver.find_elements_by_class_name(
    #         class_name)) == 0)
    #
    # def wait_presence(self, locator):
    #     # локатор в формате (By.LOCATOR, 'locator')
    #     web_element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))
    #     web_element.click()
    #     return web_element















