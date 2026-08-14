from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
import config

class WebDriverFactory:
    @staticmethod
    def get_driver(browser_name: str):
        browser_name = browser_name.lower().strip()
        if browser_name == "chrome":
            options = ChromeOptions()
            options.binary_location = config.CHROME_PATH
            service = ChromeService(executable_path=config.DRIVER_PATH)
            return webdriver.Chrome(service=service, options=options)
        elif browser_name == "firefox":
            return webdriver.Firefox()
        elif browser_name == "edge":
            return webdriver.Edge()
        else:
            raise ValueError(f"Браузер '{browser_name}' не поддерживается фабрикой.")
