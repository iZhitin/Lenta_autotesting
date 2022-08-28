# импортируем базовый класс для наследования всего основного функционала
from pages.base_page import BasePage
# для удобной работы с локаторами импортируем метод By
from selenium.webdriver.common.by import By


# класс главной страницы
class MainPage(BasePage):
    def __init__(self, driver, url='', timeout=10):
        if url is True:
            self.url = url
        if url is False:
            self.url = "https://lenta.com/"
        super().__init__(driver, self.url)

        # локаторы элементов страницы
        # этот локатор не только в этом классе
        self.cookie_agree_button = (By.XPATH, '//*[text()="Согласен"]')

        # header
        # баннер, ведущий в каталог
        self.go_to_catalog_from_ad = (By.XPATH,
                         '//*[@href="https://lenta.com/catalog/?utm_source=lweb&utm_medium=banner&utm_campaign=up"]')
        self.stores = (By.XPATH, "//*[@class='header-switcher__label' and text()='Магазины']")
        self.delivery = (By.XPATH, "//*[@class='header-switcher__label' and text()='Доставка']")
        self.catalog = (By.CSS_SELECTOR, '[href="/catalog/"]')
        self.header_logo = (By.CSS_SELECTOR, '.header__logo')
        self.search_icon = (By.CSS_SELECTOR, '.icon.header__search-bar-icon') # продублирован ниже
        self.profile_icon = (By.XPATH, '//*[@href="/npl/authentication"]')
        self.liked_icon = (By.XPATH, '//*[@href="/shoppinglist/"]')
        self.cart_icon = (By.XPATH, '//*[@href="/order/cart/"]')
        # адрес на главной странице в хэдере
        self.address = (By.CSS_SELECTOR, ".address-container__adress-location")

        # элементы всплывающего окна после нажатия кнопок "магазины" или "доставка"
        # всплывающая форма после нажатия на "магазины"
        self.store_window = (By.CSS_SELECTOR, '.modal__content-container')
        # или на один дочерний элемент ниже self.store_window = (By.CSS_SELECTOR, '.store-picker')
        # всплывающая форма после нажатия на "доставка"
        self.delivery_window = (By.CSS_SELECTOR, '.modal__content-container')
        # внутренняя кнопка "Магазины / Самовывоз" во всплывающей форме
        self.inner_store_button = (By.XPATH, '//*[text()="Магазины / Самовывоз"]')
        # внутренняя кнопка "Доставка" во всплывающей форме
        self.inner_delivery_button = (By.XPATH, '//*[text()="Доставка"]')
        self.inner_address_input_field = (By.CSS_SELECTOR, 'input.input-field__control.input-field__control--native')
        self.address_confirmation_button = (By.CSS_SELECTOR, '.button.button--primary.button--small.buttons-control__button.delivery-flow__submit')
        self.inner_show_addresses_by_list_button = (By.CSS_SELECTOR, '.button.button--primary.button--small.buttons-control__button.stores-flow__button')
        self.dropped_list_of_store_addresses = (By.CSS_SELECTOR, '.stores-list-item__name')
        self.inner_choose_store_button = (By.CSS_SELECTOR, '.button.button--primary.button--small.buttons-control__button.store-view__button')

        # first banner
        # кнопки для пролистывания акций баннера
        self.right_buttons = (By.XPATH, '//*[@class="swiper-slider-button-next"]')
        self.left_buttons = (By.XPATH, '//*[@class="swiper-slider-button-prev"]')
        # одна из 5 акций баннера
        self.selection_board = (By.XPATH,
                          '//*[@src="https://lenta.servicecdn.ru/globalassets/slider-images/2022-06/1326x300__american-tourister_samsonite______.jpg"]')

        # элементы поиска
        # поиск во внешнем поле (при масштабе 100%)
        self.search_field = (By.CSS_SELECTOR, '.catalog-search__field')
        self.search_icon_button = (By.CSS_SELECTOR, '.catalog-search__icon')
        # поиск во внутреннем поле (при масштабе 110%)
        self.search_icon = (By.CSS_SELECTOR, '.icon.header__search-bar-icon')
        self.inner_search_field = (By.CSS_SELECTOR, '.catalog-search-popup__input')
        # результаты поиска
        self.successful_search_results = (By.XPATH, '//*[text()="Результаты поиска"]')
        self.unsuccessful_search_results = (By.XPATH, '//*[text()="Мы ничего не нашли"]')

        # footer
        # ссылка на политику конфиденциальности
        self.privacy_policy = (By.XPATH, '//*[@href="/pokupatelyam/privacy-policy/" and @class="footer__policy-link"]')
        # контакты
        self.phone_link = (By.CSS_SELECTOR, '.footer__contact-tel')
        self.telegram_icon_link = (By.XPATH, '//*[@ga-event-label="Telegram"]')
        self.whatsapp_icon_link = (By.XPATH, '//*[@ga-event-label="WhatsApp"]')
        # заголовки (ссылки) столбцов со ссылками
        self.about_company = (By.CSS_SELECTOR, '.footer__main-nav.main-nav [href="/o-kompanii/"]')
        self.to_customers = (By.CSS_SELECTOR, '.footer__main-nav.main-nav [href="/pokupatelyam/"]')
        self.to_legal_persons = (By.CSS_SELECTOR, '.footer__main-nav.main-nav [ga-event-label="Юридическим лицам"]')
        # 18 ссылок в футере (под "о компании", "покупателям" и "юридическим лицам")
        self.footer_links = (By.CSS_SELECTOR, '.footer__main-nav.main-nav .main-nav__item-select [ga-event-action="goToPage"]')
        # оценка работы сайта
        self.estimate_website = (By.CSS_SELECTOR, ".footer__feedback-button")
        self.feedback_form = (By.CSS_SELECTOR, ".feedback-form__help-message")
        # ссылки на мобильные приложения
        self.mobile_applications = (By.CSS_SELECTOR, ".footer__mobile-app")
        # ссылки на соцсети
        self.social_medias = (By.CSS_SELECTOR, '.footer__social-panel-item')

        # этот локатор не только в этом классе
        self.add_to_basket_button = (By.CSS_SELECTOR, '.sku-card-small-basket-control__default-control')

        # карточка товара
        self.product_card = (By.CSS_SELECTOR, '.sku-card-small-container')

        # количество (цифра у корзины) добавленных товаров
        # этот локатор не только в этом классе
        self.amount_of_goods = (By.CSS_SELECTOR, ".header-catalog-link__counter.js-sku-counter-basket.header-catalog-link__counter--show")

        # блок с позициями в открытой корзине
        self.content_of_basket = (By.CSS_SELECTOR,  '.sku-card-in-basket')

        # авторизацию не получится использовать, так как нужны смс из телефона
