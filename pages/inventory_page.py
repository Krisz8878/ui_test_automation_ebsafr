import logging
from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_names = (By.CLASS_NAME, "inventory_item_name")
        self.sort_dropdown = (By.CLASS_NAME, "product_sort_container")

    def get_product_names(self):
        logging.info("Fetching product names.")
        elements = self.driver.find_elements(*self.product_names)
        product_names = [element.text for element in elements]
        logging.info(f"Product names: {product_names}")
        return product_names

    def change_sort_order(self, option_value):
        logging.info(f"Changing sort order to {option_value}.")
        dropdown = self.driver.find_element(*self.sort_dropdown)
        dropdown.click()
        dropdown.find_element(By.CSS_SELECTOR, f"option[value='{option_value}']").click()