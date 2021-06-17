from .base_page import BasePage
from .locators import BasketPageLocators
import pytest

class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.IS_BASKET_EMPTY), \
            "Basket is not empty!"

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), \
            "There is no 'Your basket is empty' text!"