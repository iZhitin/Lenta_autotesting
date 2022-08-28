Introduction
============
Данный репозиторий предназначен для автоматизированного тестирования сайта сети магазинов ["Лента"](https://lenta.com/)
<br>
Отображено 36 тестовых случаев разной сложности и продолжительности, 2 из которых - параметризация более 1500 поисковых запросов
<br>
Фреймворк и тесты были написаны в течение 5 дней

How To Run Tests
================
Для взаимодействия необходимо скопировать репозиторий и установить библиотеки следующей командой в терминале:
```
pip install -r requirements.txt
```

Для запуска тестовых наборов по маркеру:
```
python -m pytest -m 'marker' -v --driver Chrome --driver-path chromedriver.exe
```
Полный список маркеров представлен в файле pytest.ini
<br>
<br>
Для запуска пользовательского сценария:
```
python -m pytest -m 'user' -v --driver Chrome --driver-path chromedriver.exe
```
Для запуска тестирования более 1500 поисковых запросов:
```
python -m pytest -m 'long' -v --driver Chrome --driver-path chromedriver.exe
```
Для запуска тестирования элементов на кликабельность:
```
python -m pytest -m 'clickable' -v --driver Chrome --driver-path chromedriver.exe
```

Note
====
Запуск bash-скрипта cleanup.sh очищается рабочую директорию от кэша и прочих временных файлов

<!--

# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_catalog_page.py
# python -m pytest tests/test_catalog_page.py -v --driver Chrome --driver-path chromedriver.exe
# python -m pytest -m 'marker' tests/ -v --driver Chrome --driver-path chromedriver.exe
# python -m pytest -m 'marker' -v --driver Chrome --driver-path chromedriver.exe
# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests\test_catalog_page.py
# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests\test_main_page.py


Для запуска всех тестов основной главной страницы:
python -m pytest tests/test_main_page.py -v --driver Chrome --driver-path chromedriver.exe

Для запуска всех тестов страницы каталога:
python -m pytest tests/test_catalog_page.py -v --driver Chrome --driver-path chromedriver.exe

Для запуска всех тестов страницы товара:
python -m pytest tests/test_product_page.py -v --driver Chrome --driver-path chromedriver.exe

-->


