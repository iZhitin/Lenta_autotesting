# импортируем функционал применимый к любой странице
from pages.base_page import BasePage
# для удобной работы с локаторами импортируем метод By
from selenium.webdriver.common.by import By


# класс страницы каталога
class CatalogPage(BasePage):
    def __init__(self, driver, timeout=10):
        self.driver = driver
        # прибавляем к url главной страницы параметры пути ?
        page = BasePage(driver)
        self.url = page.url + 'catalog/'
        # ЕСЛИ не передать self.url в super(), то будет открываться гл. страница из BasePage
        super().__init__(driver, self.url)

        # локаторы элементов страницы

        # экранирование кавычки обратным слэшем \"
        # вместо записи By.CSS_SELECTOR используем 'css selector', так как в словаре не получается реализовать By
        # self.categories = {
        # 'meat_category' : "('css selector', 'a[href=\"/catalog/myaso-ptica-kolbasa/\"]')"
        # } # и даже так реализация словаря не работает
        # 'fruits_and_veg_category' = (By.CSS_SELECTOR, 'a[href="/catalog/frukty-i-ovoshchi/"]')
        # 'bakery_category' = (By.CSS_SELECTOR, 'a[href="/catalog/konditerskie-izdeliya/"]')
        # 'hot_beverages_category' = (By.CSS_SELECTOR, 'a[href="/catalog/chajj-kofe-kakao/"]')
        # 'grocery_category' = (By.CSS_SELECTOR, 'a[href="/catalog/bakaleya/"]')
        # 'frozen_category' = (By.CSS_SELECTOR, 'a[href="/catalog/zamorozhennaya-produkciya/"]')
        # 'milky_and_eggs_category' = (By.CSS_SELECTOR, 'a[href="/catalog/moloko-syr-yajjco/"]')
        # 'seafood_category' = (By.CSS_SELECTOR, 'a[href="/catalog/ryba-i-moreprodukty/"]')
        # 'healthy_food_category' = (By.CSS_SELECTOR, 'a[href="/catalog/zdorovoe-pitanie/"]')
        # 'own_food_category' = (By.CSS_SELECTOR, 'a[href="/catalog/produkciya-sobstvennogo-proizvodstva/"]')
        # 'soft_drinks_category' = (By.CSS_SELECTOR, 'a[href="/catalog/bezalkogolnye-napitki/"]')
        # 'alcohol_category' = (By.CSS_SELECTOR, 'a[href="/catalog/alkogolnye-napitki/"]')
        # 'bread_category' = (By.CSS_SELECTOR, 'a[href="/catalog/hleb-i-hlebobulochnye-izdeliya/"]')
        # 'beauty_and_health_category' = (By.CSS_SELECTOR, 'a[href="/catalog/krasota-i-zdorove/"]')
        # 'household_chemicals_category' = (By.CSS_SELECTOR, 'a[href="/catalog/bytovaya-himiya/"]')
        # 'sport_category' = (By.CSS_SELECTOR, 'a[href="/catalog/sport-i-aktivnyjj-otdyh/"]')
        # 'for_pets_category' = (By.CSS_SELECTOR, 'a[href="/catalog/tovary-dlya-zhivotnyh/"]')
        # 'zoomarket_category' = (By.CSS_SELECTOR, 'a[href="/catalog/lenta-zoomarket---professionalnyjj-uhod/"]')
        # 'for_cars_category' = (By.CSS_SELECTOR, 'a[href="/catalog/avtotovary/"]')
        # 'appliances_category' = (By.CSS_SELECTOR, 'a[href="/catalog/bytovaya-tehnika-i-elektronika/"]')
        # 'dacha_category' = (By.CSS_SELECTOR, 'a[href="/catalog/dacha-sad/"]')
        # 'for_kids_category' = (By.CSS_SELECTOR, 'a[href="/catalog/tovary-dlya-detejj/"]')
        # 'for_home_category' = (By.CSS_SELECTOR, 'a[href="/catalog/vse-dlya-doma/"]')
        # 'utensils_category' = (By.CSS_SELECTOR, 'a[href="/catalog/posuda/"]')
        # 'clothes_category' = (By.CSS_SELECTOR, 'a[href="/catalog/odezhda-i-obuv/"]')
        # 'office_category' = (By.CSS_SELECTOR, 'a[href="/catalog/kancelyariya-i-pechatnaya-produkciya/"]')
        # 'textile_category' = (By.CSS_SELECTOR, 'a[href="/catalog/tekstil-dlya-doma/"]')
        # 'flowers_category' = (By.CSS_SELECTOR, 'a[href="/catalog/cvety/"]')
        # 'tobacco_category' = (By.CSS_SELECTOR, 'a[href="/catalog/tabachnaya-produkciya/"]')
        # }

        self.meat_category = (By.CSS_SELECTOR, 'a[href="/catalog/myaso-ptica-kolbasa/"]')
        self.fruits_and_veg_category = (By.CSS_SELECTOR, 'a[href="/catalog/frukty-i-ovoshchi/"]')
        self.bakery_category = (By.CSS_SELECTOR, 'a[href="/catalog/konditerskie-izdeliya/"]')
        self.hot_beverages_category = (By.CSS_SELECTOR, 'a[href="/catalog/chajj-kofe-kakao/"]')
        self.grocery_category = (By.CSS_SELECTOR, 'a[href="/catalog/bakaleya/"]')
        self.frozen_category = (By.CSS_SELECTOR, 'a[href="/catalog/zamorozhennaya-produkciya/"]')
        self.milky_and_eggs_category = (By.CSS_SELECTOR, 'a[href="/catalog/moloko-syr-yajjco/"]')
        self.seafood_category = (By.CSS_SELECTOR, 'a[href="/catalog/ryba-i-moreprodukty/"]')
        self.healthy_food_category = (By.CSS_SELECTOR, 'a[href="/catalog/zdorovoe-pitanie/"]')
        self.own_food_category = (By.CSS_SELECTOR, 'a[href="/catalog/produkciya-sobstvennogo-proizvodstva/"]')
        self.soft_drinks_category = (By.CSS_SELECTOR, 'a[href="/catalog/bezalkogolnye-napitki/"]')
        self.alcohol_category = (By.CSS_SELECTOR, 'a[href="/catalog/alkogolnye-napitki/"]')
        self.bread_category = (By.CSS_SELECTOR, 'a[href="/catalog/hleb-i-hlebobulochnye-izdeliya/"]')
        self.beauty_and_health_category = (By.CSS_SELECTOR, 'a[href="/catalog/krasota-i-zdorove/"]')
        self.household_chemicals_category = (By.CSS_SELECTOR, 'a[href="/catalog/bytovaya-himiya/"]')
        self.sport_category = (By.CSS_SELECTOR, 'a[href="/catalog/sport-i-aktivnyjj-otdyh/"]')
        self.for_pets_category = (By.CSS_SELECTOR, 'a[href="/catalog/tovary-dlya-zhivotnyh/"]')
        self.zoomarket_category = (By.CSS_SELECTOR, 'a[href="/catalog/lenta-zoomarket---professionalnyjj-uhod/"]')
        self.for_cars_category = (By.CSS_SELECTOR, 'a[href="/catalog/avtotovary/"]')
        self.appliances_category = (By.CSS_SELECTOR, 'a[href="/catalog/bytovaya-tehnika-i-elektronika/"]')
        self.dacha_category = (By.CSS_SELECTOR, 'a[href="/catalog/dacha-sad/"]')
        self.for_kids_category = (By.CSS_SELECTOR, 'a[href="/catalog/tovary-dlya-detejj/"]')
        self.for_home_category = (By.CSS_SELECTOR, 'a[href="/catalog/vse-dlya-doma/"]')
        self.utensils_category = (By.CSS_SELECTOR, 'a[href="/catalog/posuda/"]')
        self.clothes_category = (By.CSS_SELECTOR, 'a[href="/catalog/odezhda-i-obuv/"]')
        self.office_category = (By.CSS_SELECTOR, 'a[href="/catalog/kancelyariya-i-pechatnaya-produkciya/"]')
        self.textile_category = (By.CSS_SELECTOR, 'a[href="/catalog/tekstil-dlya-doma/"]')
        self.flowers_category = (By.CSS_SELECTOR, 'a[href="/catalog/cvety/"]')
        self.tobacco_category = (By.CSS_SELECTOR, 'a[href="/catalog/tabachnaya-produkciya/"]')


        # локаторы элементов элементов страницы
        # этот локатор не только в этом классе
        self.add_to_busket_button = (By.CSS_SELECTOR, '.sku-card-small-basket-control__default-control')
        # self.add_to_busket_button = (By.CSS_SELECTOR, '.sku-card-small-basket-control__default-control')
        # self.add_to_busket_button = (By.XPATH, '//*[text()="В корзину"]')
        # self.add_to_busket_button = (By.CSS_SELECTOR, '.sku-card-small-basket-control.sku-card-small__control')

        # этот локатор не только в этом классе
        self.cookie_agree_button = (By.XPATH, '//*[text()="Согласен"]')

        # количество (цифра у корзины) добавленных товаров
        # этот локатор не только в этом классе
        self.amount_of_goods = (By.CSS_SELECTOR, ".header-catalog-link__counter.js-sku-counter-basket.header-catalog-link__counter--show")





