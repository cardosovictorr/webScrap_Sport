from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROME_DRIVER_PATH = '/Users/martinle/Downloads/chromedriver'


class SeleniumDriver(ABC):

    def __init__(self):
        options = Options()
        options.headless = True
        self._driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, chrome_options=options)

    def cleanup(self):
        self._driver.quit()
        self._driver = None
