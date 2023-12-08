from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_empty(self):
        self.should_be_empty_message()
        self.should_not_be_products_with_empty_basket()
        self.should_not_be_products_without_adding()

    def should_be_empty_message(self):
        empty_message = self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE).text
        print(empty_message)
        assert "Your basket is empty." in empty_message, "Message that the basket is empty, missing, or different"

    def should_not_be_products_with_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Products are presented, but should not be"

    def should_not_be_products_without_adding(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "Products aren't presented and should not be"


