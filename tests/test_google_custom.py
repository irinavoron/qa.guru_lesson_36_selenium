from selenium.webdriver import Keys

from seleyasha import match
from seleyasha import browser
from seleyasha.browser import assert_, element, type_to_element, click_element

browser.open('https://www.ecosia.org/')

type_to_element('[name=q]', value='releases selene yashaka' + Keys.ENTER)
element('[data-test-id=mainline-result-web]:nth-of-type(1) a').click()
click_element('[id=pull-requests-tab]')
assert_(match.number_of_elements('a[id^="issue_"]', 0))

browser.quit()
