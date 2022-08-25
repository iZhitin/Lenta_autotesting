# для работы с cookie
import pickle
# загрузка кук из файла
with open("my_cookies.txt", "rb") as cookiesfile:
    cookies = pickle.load(cookiesfile)
    for cookie in cookies:
        selenium.add_cookie(cookie)
selenium.refresh()
# выгрузка кук в файл
with open("my_cookies.txt", "wb") as cookies:
    pickle.dump(selenium.get_cookies(), cookies)