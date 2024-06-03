from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import _element_if_visible

from seleyasha import shared
from seleyasha.selector import to_locator


def element(selector):
    def command(driver):
        return _element_if_visible(driver.find_element(*to_locator(selector)))

    return shared.wait.until(command)


def type_to_element(selector, value):
    def predicate(driver: WebDriver):
        webelement = driver.find_element(*to_locator(selector))
        # driver.execute_script()
        webelement.send_keys(value)
        return True

    return shared.wait.until(predicate)


def click_element(selector):
    def command(driver: WebDriver):
        driver.find_element(*to_locator(selector)).click()
        return True

    return shared.wait.until(command)
