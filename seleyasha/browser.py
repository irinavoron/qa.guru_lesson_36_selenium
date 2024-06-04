from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import _element_if_visible
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from dataclasses import dataclass

from seleyasha.selector import to_locator

@dataclass
class Config:
    timeout = 5


class Browser:
    def __init__(self, driver, config=Config()):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.config = config
        self.wait = WebDriverWait(driver, timeout=config.timeout, ignored_exceptions=(WebDriverException,))

    def assert_(self, condition):
        return self.wait.until(condition)

    def open(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

    def element(self, selector):
        def command(driver):
            return _element_if_visible(driver.find_element(*to_locator(selector)))

        return self.wait.until(command, message=f'element by {selector} isn`t ready')

    def type_to_element(self, selector, value):
        def predicate(driver: WebDriver):
            webelement = driver.find_element(*to_locator(selector))
            # driver.execute_script()
            webelement.send_keys(value)
            return True

        return self.wait.until(predicate, message=f'failed to type into element by {selector}')

    def click_element(self, selector):
        def command(driver: WebDriver):
            driver.find_element(*to_locator(selector)).click()
            return True

        return self.wait.until(command, message=f'failed to click element by {selector}')
