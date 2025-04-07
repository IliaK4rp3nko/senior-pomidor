from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage

def test_add_items_and_checkout(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)
    checkout_overview_page = CheckoutOverviewPage(page)
    checkout_complete_page = CheckoutCompletePage(page)
    
    login_page.login('standard_user', 'secret_sauce')
    inventory_page.add_first_item_to_card()
    checkout_page.start_checkout()
    checkout_page.fill_checkoout_form('Ilia', 'Karpenko', '23456789')
    checkout_page.click_continue_button()
    checkout_overview_page.assert_checkout_overview_elements_present()
    checkout_overview_page.finish_button_click()
    checkout_complete_page.assert_order_complete_page_elements_present()
    checkout_complete_page.click_burger_menu()
    checkout_complete_page.logout()
     
    