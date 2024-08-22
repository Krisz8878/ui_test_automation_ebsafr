import logging

class Config:
    BASE_URL = "https://www.saucedemo.com/"
    USERNAME = "standard_user"
    PASSWORD = "secret_sauce"
    BROWSER = "chrome"  # Can be 'chrome', 'firefox', etc.

    # Logging configuration (optional)
    LOG_LEVEL = logging.INFO
    LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

# Set up logging based on configuration
logging.basicConfig(level=Config.LOG_LEVEL, format=Config.LOG_FORMAT)