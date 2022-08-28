# Lenta_autotesting
This repository contains code for automatic testing of the LENTA online store

Для запуска тестов необходимо скопировать репозиторий и установить библиотеки командой в терминале:
pip install -r requirements.txt

Для запуска тестов по маркеру нужно воспользоваться командой:
python -m pytest -m 'markerrr' tests/ -v --driver Chrome --driver-path chromedriver.exe
или
python -m pytest -m 'markerrr' -v --driver Chrome --driver-path chromedriver.exe

# для запуска тестов через терминал:
# 
# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_catalog_page.py
# python -m pytest tests/test_catalog_page.py -v --driver Chrome --driver-path chromedriver.exe
# python -m pytest -m 'marker' tests/ -v --driver Chrome --driver-path chromedriver.exe
# python -m pytest -m 'marker' -v --driver Chrome --driver-path chromedriver.exe

# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests\test_catalog_page.py

# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests\test_main_page.py


Список маркеров представлен в файле pytest.ini

Для запуска всех тестов основной главной страницы:
python -m pytest tests/test_main_page.py -v --driver Chrome --driver-path chromedriver.exe

Для запуска всех тестов страницы каталога:
python -m pytest tests/test_catalog_page.py -v --driver Chrome --driver-path chromedriver.exe

Для запуска всех тестов страницы товара:
python -m pytest tests/test_product_page.py -v --driver Chrome --driver-path chromedriver.exe

Запуск bash-скрипта cleanup.sh очищается рабочую директорию от кэша и прочего, которые появлятся после работы с файлами *.py

