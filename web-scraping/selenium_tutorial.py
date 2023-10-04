# from selenium import webdriver
# from selenium.webdriver.common.by import By

# browser = webdriver.Chrome()
# browser.get('https://inventwithpython.com')
# # print(browser) # <selenium.webdriver.chrome.webdriver.WebDriver (session="7770cc55fc657dc0b321796ca8d90b3b")>
# linkElem = browser.find_element(By.LINK_TEXT, 'Read Online for Free')
# # print(type(linkElem)) # <class 'selenium.webdriver.remote.webelement.WebElement'>
# # <class 'selenium.webdriver.remote.webelement.FirefoxWebElement'>
# linkElem.click()

# # prevents chrome browser from closing
# while True:
#     pass

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://nostarch.com')
htmlElem = browser.find_element(By.TAG_NAME, 'html')
htmlElem.send_keys(Keys.END)     # scrolls to bottom
htmlElem.send_keys(Keys.HOME)    # scrolls back to top
# This would be useful if, for example, new content is loaded once you’ve scrolled to the bottom of the page.