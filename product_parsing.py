import requests
from bs4 import BeautifulSoup

res_first = requests.get("https://calorizator.ru/product/all")
soup = BeautifulSoup(res_first.text, 'lxml')
product_list = [tag.text for tag in soup.select('td.views-field.views-field-title.active>a')]
for i in range(1, 80): # [1 : 79]
    res_others = requests.get("https://calorizator.ru/product/{0}".format(i))
    soup = BeautifulSoup(res_others.text, 'lxml')
    page_product_list = [tag.text for tag in soup.select('td.views-field.views-field-title.active>a')]
    # не работает
    # product_list.append(*page_product_list)
    for n in page_product_list:
        product_list.append(n)

with open("parsed_products.txt", "w", encoding="utf-8") as f:
    f.write(
        "product_list = {0}".format(product_list)
    )

print(len(product_list))

# for tag in soup.select('td.views-field.views-field-title.active>a'):
#     print(tag.text)

# print(soup.select('td.views-field.views-field-title.active>a').text)
