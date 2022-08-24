from pages.auth_page import AuthPage
from pages.my_pets_page import MyPetsPage

# для запуска тестов через терминал:
# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests\test_my_pets.py


# тестирование элементов хэдера
def test_my_pets(selenium):
    # авторизация
    page = AuthPage(selenium)
    page.enter_email("p@p.p")
    page.enter_password("122333")
    page.click_btn()

    # тест 1 - проверка, что клик на PetFriends в хэдере ведет другую страницу
    # создаем объект класса страницы с питомцами пользователя
    p = MyPetsPage(selenium)
    url_before = p.driver.current_url
    p.logo_header_click()
    url_after = p.driver.current_url
    assert url_before != url_after, "Клик на PetFriends в хэдере не ведет на другую страницу"

    # тест 2 - проверка, что клик на "Все питомцы" в хэдере ведет на другую страницу
    # создаем объект класса страницы со всеми животными
    p = MyPetsPage(selenium)
    url_before = p.driver.current_url
    p.all_pets_click()
    url_after = p.driver.current_url
    assert url_before != url_after, "Клик на 'Все питомцы' в хэдере не ведет на другую страницу"

    # тест 3 - проверка, что клик на "Мои питомцы" в хэдере не ведет на другую страницу
    # создаем объект класса страницы со всеми животными
    p = MyPetsPage(selenium)
    url_before = p.driver.current_url
    p.my_pets_click()
    url_after = p.driver.current_url
    assert url_before == url_after,\
        "Клик на 'Мои питомцы' в хэдере ведет на другую страницу"

    # тест 4 - проверка, что клик на "Выйти" в хэдере ведет на страницу регистрации
    # создаем объект класса страницы со всеми животными
    p = MyPetsPage(selenium)
    p.log_out_click()
    url_after_click = p.driver.current_url
    assert url_after_click == 'https://petfriends.skillfactory.ru/', \
        "Клик на кнопку 'Выйти' в хэдере не ведет на страницу авторизации"
