from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, timeout=10, ignored_exceptions=(WebDriverException,))


def assert_that(condition):
    return wait.until(condition)
