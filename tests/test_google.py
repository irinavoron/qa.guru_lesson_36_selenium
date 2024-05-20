from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.ecosia.org/')
wait = WebDriverWait(driver, timeout=10)

# def find_element(driver):
#     return driver.find_element(By.CSS_SELECTOR, '[name=q]')
#
# wait.until(find_element).send_keys('selene', Keys.ENTER)
# def element(by, selector):
#     def find_element(driver):
#         return driver.find_element(by, selector)
#
#     return find_element
#
# wait.until(
#     lambda driver: element(By.CSS_SELECTOR, '[name=q]')
# ).send_keys('selene yashaka', Keys.ENTER)
# wait.until(
#     lambda driver: element(By.CSS_SELECTOR, '[data-test-id=mainline-result-web]:nth-of-type(1) a')
# ).click()

# def element(by, selector):
#     def find_element(driver):
#         return driver.find_element(by, selector)
#
#     return find_element
#
#
# search_box = wait.until(element(By.CSS_SELECTOR, '[name=q]'))
# search_box.send_keys('selene yashaka', Keys.ENTER)
#
# first_result = wait.until(element(By.CSS_SELECTOR, '[data-test-id=mainline-result-web]:nth-of-type(1) a'))
# first_result.click()


search_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[name=q]')))
search_field.send_keys('selene yashaka', Keys.ENTER)

search_result = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, '[data-test-id=mainline-result-web]:nth-of-type(1) a')
)
)
search_result.click()
