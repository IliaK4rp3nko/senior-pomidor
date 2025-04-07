from pages.base_page import BasePage

class CheckoutOverviewPage(BasePage):
    ORDER_SUMMARY_SELECTOR = ".summary_info"
    ITEM_SELECTOR = ".cart_item"
    HEADER_SELECTOR = ".title"
    FINISH_BUTTON_SELECTOR = "#finish"
    CANCEL_BUTTON_SELECTOR = "#cancel"
    CHECKOUT_COMLETE_URL = "https://www.saucedemo.com/checkout-complete.html"
    
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = '/checkout-step-two.html'
    
    def assert_checkout_overview_elements_present(self):
        self.assert_text_in_element(self.HEADER_SELECTOR, "Checkout: Overview")
        self.assert_element_is_visible(self.ORDER_SUMMARY_SELECTOR)
        self.assert_element_is_visible(self.FINISH_BUTTON_SELECTOR)
        self.assert_element_is_visible(self.CANCEL_BUTTON_SELECTOR)
        self.assert_element_is_visible(self.ITEM_SELECTOR)
    
    def finish_button_click(self):
        self.wait_for_selector_and_click(self.FINISH_BUTTON_SELECTOR)
        self.assert_url_is_correct(self.CHECKOUT_COMLETE_URL)

    
