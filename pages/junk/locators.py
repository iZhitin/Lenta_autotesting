# для удобной работы с локаторами импортируем метод By
from selenium.webdriver.common.by import By


class AuthLocators:
    """Локаторы для элементов страницы авторизации"""
    AUTH_EMAIL = (By.ID, "email")
    AUTH_PASSWORD = (By.ID, "pass")
    AUTH_BTN = (By.CLASS_NAME, "btn-success")


class AllPetsLocators:
    """Локаторы для элементов страницы со всеми животными (главная страница)"""
    # шапка сайта
    LOGO_HEADER = (By.CSS_SELECTOR, 'a.navbar-brand.header2')
    MY_PETS = (By.XPATH, "//*[text()='Мои питомцы']")
    ALL_PETS = (By.XPATH, "//*[text()='Все питомцы']")
    LOG_OUT = (By.XPATH, "//*[text()='Выйти']")
    # тело сайта
    CENTER_TITLE = (By.CSS_SELECTOR, "div>h1[class='text-center']")
    DESCRIPTION = (By.XPATH, "//*[text()='Все питомцы наших пользователей']")
    ANIMAL_CARDS = (By.CSS_SELECTOR, "div.card")
    ANIMAL_PHOTOS = (By.CSS_SELECTOR, "img.card-img-top")
    ANIMAL_NAMES = (By.CSS_SELECTOR, ".card-title")
    ANIMAL_TYPES_AND_AGES = (By.CSS_SELECTOR, ".card-text")
    # подвала на сайте - нет


class MyPetsLocators:
    """Локаторы для элементов страницы с животными пользователя"""
    # шапка сайта
    LOGO_HEADER = (By.CSS_SELECTOR, "a.navbar-brand.header2")
    MY_PETS = (By.XPATH, "//*[text()='Мои питомцы']")
    ALL_PETS = (By.XPATH, "//*[text()='Все питомцы']")
    LOG_OUT = (By.XPATH, "//*[text()='Выйти']")
    # тело сайта
    #  меню
    NICKNAME = (By.CSS_SELECTOR, "div>h2")
    INFO_BOARD = (By.XPATH, "//div[@class='.col-sm-4 left']")
    #  шапка таблицы с животными
    PHOTO_COLUMN_TITLE = (By.XPATH, '//*[text()="Фото"]')
    NAME_COLUMN_TITLE =(By.XPATH, '//*[text()="Имя"]')
    TYPE_COLUMN_TITLE =(By.XPATH, '//*[text()="Порода"]')
    AGE_COLUMN_TITLE =(By.XPATH, '//*[text()="Возраст"]')
    #   строчки с данными о животных
    ANIMAL_BLOCKS = (By.XPATH, '//tbody/tr')
    #   данные животных
    ANIMAL_PHOTOS = (By.XPATH, '//th/img[@src]')
    ANIMAL_NAMES = (By.XPATH, '//tr/th/following-sibling::td[1]')
    ANIMAL_TYPES = (By.XPATH, '//tr/th/following-sibling::td[2]')
    ANIMAL_AGES = (By.XPATH, '//tr/th/following-sibling::td[3]')
    #   кнопка добавления животного
    ADD_ANIMAL = (By.XPATH, '//*[text()="Добавить питомца"]')
    # подвала на сайте - нет


class AddPetLocators:
    """Локаторы для элементов страницы добавления животного. Чтобы открыть страницу,
    нужно зайти на https://petfriends.skillfactory.ru/my_pets и нажать кнопку 'добавить'"""
    # заголовок
    ADDING_TITLE = (By.ID, 'addPetsModalLabel')
    # внесение данных
    ADD_PHOTO = (By.XPATH, '//input[@type="file"]')
    NAME_FIELD = (By.ID, 'name')
    ANIMAL_TYPE_FIELD = (By.ID, 'animal_type')
    AGE_FIELD = (By.ID, 'age')
    # кнопки
    CLOSE_CROSS = (By.CSS_SELECTOR, "span[aria-hidden='true']")
    CLOSE_BTN = (By.XPATH, '//*[text()="Отмена"]')
    SUBMIT_BTN = (By.XPATH, '//*[@onclick="add_pet();"]')

