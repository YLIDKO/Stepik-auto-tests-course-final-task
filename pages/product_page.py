from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "There is no 'add to cart'   button"

    def get_name_of_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text


    def add_product_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        add_to_cart_button.click()


    def solve_quiz_and_get_code(self):
        self.alert_quiz()


    def should_be_success_message(self):
        add_to_basket_message = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_MES).text
        assert add_to_basket_message == self.get_name_of_product(), "Wrong product was added"


    def cost_of_product(self):
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_COST).text
        assert product_cost == basket_cost.split()[2], "The prices are not equal"


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"


    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"