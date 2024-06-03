from selenium.webdriver import Keys

from seleyasha.conditions import number_of_elements
from seleyasha.command import element, type_to_element, click_element
from seleyasha import shared
from seleyasha.shared import assert_that

shared.driver.get('https://www.ecosia.org/')

type_to_element('[name=q]', value='releases selene yashaka' + Keys.ENTER)
element('[data-test-id=mainline-result-web]:nth-of-type(1) a').click()
click_element('[id=pull-requests-tab]')
assert_that(number_of_elements('a[id^="issue_"]', 0))

shared.driver.quit()
