from pages.base_page import BasePage

class CheckoutCompletePage(BasePage):
    ORDER_COMPLETE_HEADER = ".title"
    THANK_YOU_TEXT = "h2.complete-header"
    ORDER_COMPLETE_MESSAGE = ".complete-text"
    SUCCESS_ICON = ".pony_express"
    BACK_HOME_BUTTON = "#back-to-products"
    BURGER_MENU_BUTTON = "#react-burger-menu-btn"
    ALL_ITEMS_BUTTON = '#inventory_sidebar_link'
    ABOUT_BUTTON = '#about_sidebar_link'
    LOGOUT_BUTTON = '[data-test="logout-sidebar-link"]'
    RESET_APP_STATE_BUTTON = '#reset_sidebar_link'
    LOGOUT_URL = "https://www.saucedemo.com/"
    
    
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = '/checkout-complete.html'

    def assert_order_complete_page_elements_present(self):
        self.assert_text_in_element(self.ORDER_COMPLETE_HEADER, "Checkout: Complete!")
        self.assert_text_in_element(self.THANK_YOU_TEXT, "Thank you for your order!")
        self.assert_element_is_visible(self.ORDER_COMPLETE_MESSAGE)
        self.assert_element_is_visible(self.SUCCESS_ICON)
        self.assert_element_is_visible(self.BACK_HOME_BUTTON)
    
    def click_burger_menu(self):
        self.wait_for_selector_and_click(self.BURGER_MENU_BUTTON)
        self.assert_element_is_visible(self.ALL_ITEMS_BUTTON)
        self.assert_element_is_visible(self.ABOUT_BUTTON)
        self.assert_element_is_visible(self.LOGOUT_BUTTON)
        self.assert_element_is_visible(self.RESET_APP_STATE_BUTTON)
    
    def logout(self):
        self.wait_for_selector_and_click(self.LOGOUT_BUTTON)
        self.assert_url_is_correct(self.LOGOUT_URL)
    
    
    