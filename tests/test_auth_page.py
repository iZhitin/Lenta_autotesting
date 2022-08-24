# from pages.auth_page import AuthPage
from pages.main_page import MainPage
# для визуального контроля
import time
# для работы с cookie
import pickle

# для удобной работы с локаторами импортируем метод By
from selenium.webdriver.common.by import By

# для запуска тестов через терминал:
# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests\test_auth_page.py


# тестирование авторизации
# def test_auth_page(selenium):
#     page = AuthPage(selenium)
#     time.sleep(3)
#     page.enter_email("p@p.p")
#     page.enter_password("122333")
#     page.click_btn()
#     # сохраним cookie после авторизации в файл
#     with open("my_cookies.txt", "wb") as cookies:
#         pickle.dump(selenium.get_cookies(), cookies)
#
#     assert page.get_relative_link() == '/all_pets', 'Ошибка авторизации'


# from selenium import webdriver
# driver = webdriver.Chrome()

import uuid
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# page = MainPage(selenium)
# тестирование авторизации
def test_main_page(selenium):
    page = MainPage(selenium)
    # page.get_url("https://lenta.com/")
    page.get_url("https://lenta.com/")
    selenium.find_element_by_xpath\
        ('//*[@href="https://lenta.com/catalog/?utm_source=lweb&utm_medium=banner&utm_campaign=up"]').click()
    element = selenium.find_element(By.CSS_SELECTOR, 'a[href="/catalog/myaso-ptica-kolbasa/"]')
    # element = selenium.find_element(By.XPATH, '//*[text()="Мясо, птица, колбаса"]')
    # element.click()
    # selenium.scroll_to_element(element)
    page.scroll_wait_and_click_on_element((By.CSS_SELECTOR, 'a[href="/catalog/myaso-ptica-kolbasa/"]'))

    # page.take_screenshot()
    # screenshot = 'screenshots/{0}.png'
    # a = driver.save_screenshot(screenshot.format(str(uuid.uuid4().hex)))
    # screenshot = 'screenshots/{0}.png'
    # selenium.screenshot_as_png
    # selenium.get_screenshot_as_file('/screenshot/sdrfdsf.png')
    # selenium.save_screenshot('screenshots/sdrfdsf.png')
    page.take_screenshot()
    time.sleep(5)
    assert a is True



    # assert element.is_displayed() is False
    # element.click()
    # button = selenium.find_elements_by_xpath(
    #     '//button[@class="sku-card-small-basket-control__default-control"]')
    # catalog = selenium.find_element_by_xpath('//*[@href="/catalog/"]')
    # selenium.move_to_element(catalog)
    # for i in range(len(a)):
    #     a[i].click()
    # a[30].click()
    # selenium.implicitly_wait(10)
    # ActionChains(selenium).move_to_element(button[30]).click(button).perform()
    # with open("my_cookies.txt", "wb") as cookies:
    #     pickle.dump(selenium.get_cookies(), cookies)
    # for i in range(len(button)):
    #     with open('suk.txt', 'w') as file:
    #         file.write(str(button) + '\n')
    # selenium.find_element_by_xpath('//*[@href="https://lenta.com/catalog/?utm_source=lweb&utm_medium=banner&utm_campaign=up"]').click()
    # time.sleep(4)
    # # element = selenium.find_element_by_xpath('//*[@href="/catalog/myaso-ptica-kolbasa/"]')
    # element = selenium.find_element(By.XPATH, '//*[text()="Мясо, птица, колбаса"]')
    # assert element is False
    # ActionChains(selenium).move_to_element(element).click_and_hold(1).perform()
    # time.sleep(4)
    #
    # a = selenium.find_element_by_xpath('//*[@class="sku-card-small-basket-control__default-control"]')[0].click()
    # for i in range(len(a)):
    #     with open('suk.txt', 'w') as file:
    #         file.write((str(a[i]) + '\n\n'))
    # selenium.find_element(By.CLASS_NAME, 'c1adv4qi t18stym3 bw441np m493tk9 m1gxt7o n10d4det l14lhr1r').click()





def ttest_second_page(selenium):
    page = MainPage(selenium)
    # page.get_url("https://lenta.com/")
    page.get_url("https://lenta.com/")
    with open("my_cookies.txt", "rb") as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            selenium.add_cookie(cookie)
    # selenium.get('https://petfriends.skillfactory.ru/all_pets')
    selenium.refresh()
    time.sleep(5)
    assert True



