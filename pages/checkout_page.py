from pages.base_page import BasePage

class CheckoutPage(BasePage):
    CHECKOUT_BUTTON_SELECTOR = '[id="checkout"] '
    FIRST_NAME_SELECTOR = "#first-name"
    LAST_NAME_SELECTOR = "#last-name"
    POSTAL_CODE_SELECTOR = 'input[name="postalCode"]'
    CONTINUE_BUTTON = "#continue"
    CHECKOUT_OVERVIEW_URL = "https://www.saucedemo.com/checkout-step-two.html"
    
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = '/checkout-step-one.html'
    
    def start_checkout(self):
        self.wait_for_selector_and_click(self.CHECKOUT_BUTTON_SELECTOR)
        self.assert_element_is_visible(self.FIRST_NAME_SELECTOR)
    
    def fill_checkoout_form(self, firstname, lastname, postal_code):
        self.wait_for_selector_and_type(self.FIRST_NAME_SELECTOR, firstname, 100)
        self.wait_for_selector_and_type(self.LAST_NAME_SELECTOR, lastname, 100)
        self.wait_for_selector_and_type(self.POSTAL_CODE_SELECTOR, postal_code, 100)
        self.assert_input_value(self.POSTAL_CODE_SELECTOR, postal_code)
    
    def click_continue_button(self):
        self.assert_element_is_visible(self.CONTINUE_BUTTON)
        self.wait_for_selector_and_click(self.CONTINUE_BUTTON)
        self.assert_url_is_correct(self.CHECKOUT_OVERVIEW_URL)

