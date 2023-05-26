import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://katapultpro.com/map/#-NVj5c3UJChii6bl29uW")
#element = WebDriverWait(driver, timeout=10).until(lambda d: d.
# time.sleep(10)
element = driver.find_element(By.TAG_NAME, "input")
print(type(element))
print(element)

for e in element:
    print(e)
find_element = driver.find_element(By.ID, '')


find_element.send_keys('(RFL)(JA) CC23-00108-NB-I')
find_element = driver.find_element(By.ID, 'input')

find_element.send_keys('(RFL)(JA) CC23-00108-NB-I')

find_element = driver.find_element(By.ID, 'input')

find_element.send_keys('(RFL)(JA) CC23-00108-NB-I')


driver.close()

driver.get('https://katapultpro.com/map/#-NVj5c3UJChii6bl29uW')
driver.maximize_window() # For maximizing window
clickable = driver.find_element(By.TAG_NAME, "input")
print(clickable)
ActionChains(driver)\
    .double_click(clickable)\
    .perform()
print("it worked")

clickable = driver.find_element(By.CLASS, "moveContainer")
print(clickable)
ActionChains(driver)\
    .double_click(clickable)\
    .perform()

import pyautogui
pyautogui.PAUSE = 30

button = pyautogui.locateOnScreen('https://maps.gstatic.com/mapfiles/transparent.png')
print(button)