#!/usr/bin/python3
# -*- encoding=utf8 -*-

# первая строчка позволяет запускать код на разных OS, в случае если интерпретатор установлен в разных локациях
# вторая строка устанавливает кодировку

# это специальный файл, в котором прописаны функции, которые автоматически применяются к тестам

# This is example shows how we can manage failed tests
# and make screenshots after any failed test case.

# для тестирования
import pytest
# для репортирования результатов
import allure
# для присвоения id
import uuid


# параметры браузера во время теста
@pytest.fixture
def chrome_options(chrome_options):
    # chrome_options.binary_location = '/usr/bin/google-chrome-stable'
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--log-level=DEBUG')
    return chrome_options


# ???
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Фикстура передает информацию об упавших тестах в teardown"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def web_browser(request, selenium):
    """Фикстура настраивает размер окна браузера и, в случае падения тестов,
    делает скриншот и выводит логи"""
    # setUp
    browser = selenium
    browser.set_window_size(1400, 1000)
    # исполнение
    yield browser
    # tearDown (код ниже исполняется после каждого теста)
    # если тест падает: ???
    if request.node.rep_call.failed:
        # попытка сделать скриншот
        try:
            # при помощи js-скрипта обеляем бэкграунд
            browser.execute_script("document.body.bgColor = 'white';")
            # сохранение скриншота с уникальным id в папку screenshots
            browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')
            # прикрепление скриншота к allure-отчету
            allure.attach(browser.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
            # информация для успешной отладки
            print('URL: ', browser.current_url)
            print('Browser logs:')
            # вывод логов
            for log in browser.get_log('browser'):
                print(log)
        # пример отличного антипаттерна
        except:
            pass


def get_test_case_docstring(item):
    """ Эта функция получает описание из тест-кейса и форматирует его,
    чтобы показывать вместо имени тест-кейса в отчетах"""

    full_name = ''
    # ? непонятно, что здесь делает объект
    if item._obj.__doc__:
        # удаление лишних пробелов - как работает непонятно ?
        name = str(item._obj.__doc__.split('.')[0]).strip()
        full_name = ' '.join(name.split())

        # генерация списка параметров для параметризованных тест-кейсов ?
        if hasattr(item, 'callspec'):
            params = item.callspec.params

            res_keys = sorted([k for k in params])
            # создание списка основанного на словаре
            res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
            # добавление словаря со всеми параметрами к имени тест-кейса
            full_name += ' Parameters ' + str(', '.join(res))
            full_name = full_name.replace(':', '')

    return full_name


# ???
def pytest_itemcollected(item):
    """ Эта функция изменяет имена тест-кейсов "на лету" во время их выполнения"""

    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)


# ???
def pytest_collection_finish(session):
    """Эта функция изменила имена тест-кейсов "на лету" при использовании параметра --collect-only для pytest
        (чтобы получить полный список всех существующих тест-кейсов)"""

    if session.config.option.collectonly is True:
        for item in session.items:
            # если тест-кейс содержит строку doc, нам нужно изменить его имя на
            # это строка doc, чтобы показывать удобочитаемые отчеты и
            # автоматически импортировать тест-кейсы в систему управления тестированием
            if item._obj.__doc__:
                full_name = get_test_case_docstring(item)
                print(full_name)

        pytest.exit('Done!')
