from selenium.webdriver import Keys
from selenium import webdriver
from seleyasha import match
from seleyasha import browser
from seleyasha.browser import Browser
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = Browser(webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())))
browser.open('https://www.ecosia.org/')

browser.type_to_element('[name=q]', value='releases selene yashaka' + Keys.ENTER)
browser.element('[data-test-id=mainline-result-web]:nth-of-type(1) a').click()
browser.click_element('[id=pull-requests-tab]')
browser.assert_(match.number_of_elements('a[id^="issue_"]', 0))

browser.quit()
