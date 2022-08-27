#!/usr/bin/python3

import lxml
from bs4 import BeautifulSoup
# pip install lxml
# pip install bs4
import requests as req

with open("index.html", "r") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    print(soup.h2)
    print(soup.head)
    print(soup.li)

    print("HTML: {0}, name: {1}, text: {2}".format(soup.h2,
        soup.h2.name, soup.h2.text))

    # вывести названия всех тегов
    for child in soup.recursiveChildGenerator():

        if child.name:
            print(child.name)

    # список дочерних элементов тега html
    root = soup.html

    root_childs = [e.name for e in root.children if e.name is not None]
    print(root_childs)

    # все дочерние элементы тега body
    root = soup.body

    root_childs = [e.name for e in root.descendants if e.name is not None]
    print(root_childs)

# при помощи библиотеки requests
resp = req.get("http://www.something.com")

soup = BeautifulSoup(resp.text, 'lxml')

print(soup.title)
print(soup.title.text)
print(soup.title.parent)
# красивое выравнивание
print(soup.prettify())

# элемент по тегу и id
#print(soup.find("ul", attrs={ "id" : "mylist"}))
print(soup.find("ul", id="mylist"))

# элементы по тегу
for tag in soup.find_all("li"):
        print("{0}: {1}".format(tag.name, tag.text))

# поиск всех h2 и p
tags = soup.find_all(['h2', 'p'])

for tag in tags:
    print(" ".join(tag.text.split()))


# пустые элементы
def myfun(tag):
    return tag.is_empty_element


with open("index.html", "r") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    tags = soup.find_all(myfun)
    print(tags)

# В данном примере выводится содержимое элементов, в которых есть строка с символами ‘BSD’.
with open("index.html", "r") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    strings = soup.find_all(string=re.compile('BSD'))

    for txt in strings:
        print(" ".join(txt.split()))

# CSS - селекторы
with open("index.html", "r") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    print(soup.select("li:nth-of-type(3)"))

#CSS - селектор
with open("index.html", "r") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    print(soup.select_one("#mylist"))

# Метод append() добавляет в рассматриваемый HTML-документ новый тег.
with open("index.html", "r") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    newtag = soup.new_tag('li')
    newtag.string = 'OpenBSD'

    ultag = soup.ul

    ultag.append(newtag)

    print(ultag.prettify())

# Метод insert() позволяет вставить тег в определенно выбранное место.
with open("index.html", "r") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    newtag = soup.new_tag('li')
    newtag.string = 'OpenBSD'

    ultag = soup.ul

    ultag.insert(2, newtag)

    print(ultag.prettify())

# Метод replace_with() заменяет содержимое выбранного элемента.
with open("index.html", "r") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    tag = soup.find(text="Windows")
    tag.replace_with("OpenBSD")

    print(soup.ul.prettify())

# Метод decompose() удаляет определенный тег из структуры документа и уничтожает его.
with open("index.html", "r") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    ptag2 = soup.select_one("p:nth-of-type(2)")

    ptag2.decompose()

    print(soup.body.prettify())
