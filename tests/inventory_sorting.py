# Importing required libraries
import pytest
import logging
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config import Config

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.fixture(scope="module")
def setup():
    if Config.BROWSER == "chrome":
        driver = webdriver.Chrome()
    elif Config.BROWSER == "firefox":
        driver = webdriver.Firefox()
    # Add other browser options as needed

    driver.get(Config.BASE_URL)
    logging.info(f"Navigated to {Config.BASE_URL}")
    yield driver
    driver.quit()

def test_inventory_sorting(setup):
    driver = setup

    # Login to the site
    login_page = LoginPage(driver)
    logging.info("Starting the login process.")
    login_page.login()

    # Verify items are sorted by Name (A -> Z)
    inventory_page = InventoryPage(driver)
    logging.info("Verifying products are sorted A -> Z.")
    product_names = inventory_page.get_product_names()
    logging.info(f"Product names fetched: {product_names}")
    assert product_names == sorted(product_names), "Products are not sorted A -> Z by default."

    # Change the sorting to Name (Z -> A)
    logging.info("Changing sorting order to Z -> A.")
    inventory_page.change_sort_order("za")

    # Verify items are sorted by Name (Z -> A)
    product_names = inventory_page.get_product_names()
    logging.info(f"Product names fetched after sorting: {product_names}")
    assert product_names == sorted(product_names, reverse=True), "Products are not sorted Z -> A."