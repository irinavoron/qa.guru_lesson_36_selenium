from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import _element_if_visible
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from seleyasha.selector import to_locator

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, timeout=10, ignored_exceptions=(WebDriverException,))


def assert_(condition):
    return wait.until(condition)


def open(url):
    driver.get(url)


def quit():
    driver.quit()


def element(selector):
    def command(driver):
        return _element_if_visible(driver.find_element(*to_locator(selector)))

    return wait.until(command, message=f'element by {selector} isn`t ready')


def type_to_element(selector, value):
    def predicate(driver: WebDriver):
        webelement = driver.find_element(*to_locator(selector))
        # driver.execute_script()
        webelement.send_keys(value)
        return True

    return wait.until(predicate, message=f'failed to type into element by {selector}')


def click_element(selector):
    def command(driver: WebDriver):
        driver.find_element(*to_locator(selector)).click()
        return True

    return wait.until(command, message=f'failed to click element by {selector}')
