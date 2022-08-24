# импорт базового класса
from TestingPetFriendsSeleniumSPOM.pages.base import WebPage
# импорт классов веб-элементов
from TestingPetFriendsSeleniumSPOM.pages.elements import WebElement, ManyWebElements


# элементы страницы авторизации
# для класса страницы авторизации наследуем функционал взаимодействия со страницей из класса родителя
class AuthPage(WebPage):
    # инициализация объекта
    def __init__(self, web_driver, url=''):
        url = 'http://petfriends.skillfactory.com/login'
        # для использования функционала родителями, наследуем его
        super().__init__(web_driver, url)

    email = WebElement(id='email')
    password = WebElement(id='pass')
    btn = WebElement(class_name='btn.btn-success')
