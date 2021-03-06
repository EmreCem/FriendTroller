from selenium import webdriver
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import time
import os
#you must create an env variable called geckodriver
path_to_firefoxdriver = os.environ['geckodriver']
browser = webdriver.Firefox(executable_path= path_to_firefoxdriver)
url = 'https://web.whatsapp.com/'
browser.get(url)
ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
#Add Contact name or Group name below
WebDriverWait(browser, 60,ignored_exceptions=ignored_exceptions).until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@title='FRIEND NAME HERE']")))
Chat = browser.find_element_by_xpath("//span[@title='FRIEND NAME HERE']")
Chat.click()
chatTextBox = browser.find_element(By.CSS_SELECTOR, ".DuUXI")
chatText = chatTextBox.find_element(By.CSS_SELECTOR, "._1awRl.copyable-text.selectable-text")
for i in range(3600):
    time.sleep(1)
    chatText.send_keys(str(i))
    chatText.send_keys(Keys.ENTER)