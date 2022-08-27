# импортируем функционал применимый к любой странице
from pages.base_page import BasePage
# для удобной работы с локаторами импортируем метод By
from selenium.webdriver.common.by import By


# класс главной страницы
class MainPage(BasePage):
    def __init__(self, driver, url='', timeout=10):
        if url is False:
            self.url = "https://lenta.com/"
        super().__init__(driver, url, timeout)

        # локаторы элементов страницы

        # этот локатор не только в этом классе
        self.cookie_agree_button = (By.XPATH, '//*[text()="Согласен"]')

        # header
        self.go_to_catalog_from_ad = (By.XPATH,
                         '//*[@href="https://lenta.com/catalog/?utm_source=lweb&utm_medium=banner&utm_campaign=up"]')
        self.stores = (By.XPATH, "//*[@class='header-switcher__label' and text()='Магазины']")
        # или на один дочерний элемент ниже self.store_window = (By.CSS_SELECTOR, '.store-picker')
        # локаторы одинаковые (вроде)
        self.store_window = (By.CSS_SELECTOR, '.modal__content-container')
        self.delivery_window = (By.CSS_SELECTOR, '.modal__content-container')

        self.delivery = (By.XPATH, "//*[@class='header-switcher__label' and text()='Доставка']")
        self.catalog = (By.CSS_SELECTOR, '[href="/catalog/"]')
        self.header_logo = (By.CSS_SELECTOR, '.header__logo')
        self.search_icon = (By.CSS_SELECTOR, '.icon.header__search-bar-icon') # продублирован ниже
        self.profile_icon = (By.XPATH, '//*[@href="/npl/authentication"]')
        self.liked_icon = (By.XPATH, '//*[@href="/shoppinglist/"]')
        self.cart_icon = (By.XPATH, '//*[@href="/order/cart/"]')

        # first banner
        # кнопки для пролистывания акций баннера
        self.right_buttons = (By.XPATH, '//*[@class="swiper-slider-button-next"]')
        self.left_buttons = (By.XPATH, '//*[@class="swiper-slider-button-prev"]')
        # одна из 5 акций баннера
        self.selection_board = (By.XPATH,
                          '//*[@src="https://lenta.servicecdn.ru/globalassets/slider-images/2022-06/1326x300__american-tourister_samsonite______.jpg"]')

        # элементы поиска
        # поиск во внешнем поле
        self.search_field = (By.CSS_SELECTOR, '.catalog-search__field')
        self.search_icon_button = (By.CSS_SELECTOR, '.catalog-search__icon')
        # поиск во внутреннем поле
        self.search_icon = (By.CSS_SELECTOR, '.icon.header__search-bar-icon')
        self.inner_search_field = (By.CSS_SELECTOR, '.catalog-search-popup__input')
        # результаты поиска
        self.search_results = (By.XPATH, '//*[text()="Результаты поиска"]')

        # footer
        # таких два
        # self.privacy_policy = (By.XPATH, '//*[@href="/pokupatelyam/privacy-policy/"]')
        self.privacy_policy = (By.XPATH, '//*[@href="/pokupatelyam/privacy-policy/" and @class="footer__policy-link"]')
        # 'https://lenta.com/pokupatelyam/privacy-policy/'
        self.phone_link = (By.CSS_SELECTOR, '.footer__contact-tel')
        self.telegram_icon_link = (By.XPATH, '//*[@ga-event-label="Telegram"]')
        self.whatsapp_icon_link = (By.XPATH, '//*[@ga-event-label="WhatsApp"]')
        # столбцы со ссылками
        # переступил через несколько разделов
        self.about_company = (By.CSS_SELECTOR, '.footer__main-nav.main-nav [href="/o-kompanii/"]')
        self.to_customers = (By.CSS_SELECTOR, '.footer__main-nav.main-nav [href="/pokupatelyam/"]')
        self.to_legal_persons = (By.CSS_SELECTOR, '.footer__main-nav.main-nav [ga-event-label="Юридическим лицам"]')
        # 18 ссылок в футере (под "о компании", "покупателям" и "юридическим лицам")
        self.footer_links = (By.CSS_SELECTOR, '.footer__main-nav.main-nav .main-nav__item-select [ga-event-action="goToPage"]')
        # оценка работы сайт
        self.estimate_website = (By.CSS_SELECTOR, ".footer__feedback-button")
        self.feedback_form = (By.CSS_SELECTOR, ".feedback-form__help-message")
        # мобильные приложения
        self.mobile_applications = (By.CSS_SELECTOR, ".footer__mobile-app")
        # ссылки на соцсети
        self.social_medias = (By.CSS_SELECTOR, '.footer__social-panel-item')

# '.footer__main-nav.main-nav .main-nav__item-select')
# footer__main-nav main-nav
# $x('//*[@ga-event-category="migration:header-nav"]')
# $x('//*[@href="/o-kompanii/" and @ga-event-category="migration:header-nav"]')
# $x('//*[@href="/o-kompanii/"]')
        # авторизацию не получится использовать, так как нужны смс из телефона
