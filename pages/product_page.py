from .base_page import BasePage
from .locators import ProductPageLocators
import pytest
import time


class ProductPage(BasePage):

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "There is no add to cat button"

    def get_name_of_product(self):
        product_name = self.browser.find_element_by_css_selector(".product_main h1")
        return product_name.text



    def add_product_to_cart(self):
        add_to_cart_button = self.browser.find_element_by_css_selector(".btn-add-to-basket")
        add_to_cart_button.click()
        self.solve_quiz_and_get_code()


    def should_be_success_message(self):
        add_to_basket_message = self.browser.find_element_by_xpath("//div[@class='alertinner ']/strong").text
        assert add_to_basket_message == self.get_name_of_product(), "Wrong product was added"

    def cost_of_product(self):
        product_cost = self.browser.find_element_by_css_selector(".product_main p:nth-child(2)").text
        basket_cost = self.browser.find_element_by_css_selector(".basket-mini").text
        assert product_cost == basket_cost.split()[2], "The prices are not equal"